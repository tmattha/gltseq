import typing as t
import cmath as cm


def fd_diffusion(phi):
    return 2 - 2 * cm.cos(phi)


def diag(d):
    return lambda _: d

def from_coeff(coeffs: t.Sequence[complex]) -> t.Callable[[int], complex]:
    def _coeff_inst(phi):
        value: complex = 0
        for i, c in enumerate(coeffs):
            exponential_factor = len(coeffs)//2 - i
            value += c * cm.exp(exponential_factor * 1j * phi)
        return value
    return _coeff_inst