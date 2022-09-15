import enum
import hypothesis
import hypothesis.strategies as hs
import numpy as np
import gltseq.toeplitz as toeplitz
import gltseq.specsym as specsym


@hypothesis.given(hs.integers(min_value=1, max_value=50))
def test_fd_diffusion_lhs_rhs(n):
    lhs = toeplitz.eigsum_from_symbol(specsym.fd_diffusion, n)
    rhs = toeplitz.symbol_avg(specsym.fd_diffusion)
    assert abs(lhs - rhs ) < 1e-10

@hypothesis.given(hs.integers(min_value=1, max_value=50))
def test_fd_diffusion_lhs_rhs_singular(n):
    lhs = toeplitz.singsum_from_matrix(toeplitz.toeplitz(specsym.fd_diffusion, n))
    rhs = toeplitz.symbol_avg(specsym.fd_diffusion)
    assert abs(lhs - rhs ) < 1e-10

@hypothesis.given(
    hs.floats(
        min_value=-1e-5,
        max_value=1e5,
        allow_nan=False,
        allow_infinity=False),
    hs.integers(min_value=1, max_value=50))
def test_diag_lhs_rhs(d, n):
    D = np.diag(np.repeat(d, n))
    D_toeplitz = toeplitz.toeplitz(specsym.diag(d), n)
    lhs = toeplitz.eigsum_from_matrix(D)
    # For a constant the left-hand-side simplifies.
    assert abs(lhs - d) < 1e-10
    rhs = toeplitz.symbol_avg(specsym.diag(d))
    assert abs(lhs - rhs ) < 1e-10

@hypothesis.given(hs.lists(hs.complex_numbers(min_magnitude=1e-6, max_magnitude=1e6),
    max_size=8  # needs to be quite limited, as this is SLOW!
    ).filter(lambda sample: len(sample) % 2 == 1))
def test_coeff_matrix(coeffs):
    n = len(coeffs)
    M = np.zeros((n, n), dtype=complex)
    for i, c in enumerate(coeffs):
        diag_i = i - n // 2
        M += np.diag(np.repeat(c, n - abs(diag_i)), diag_i)
    assert np.allclose(toeplitz.toeplitz(specsym.from_coeff(coeffs), n), M, atol=1e-6)