import cmath as cm
import numpy as np
import numpy.typing as npt
import scipy.linalg
import scipy.integrate
import typing as t


def symbol_avg(f: t.Callable[[float], complex]) -> float:
    f_real = lambda phi: f(phi).real
    f_imag = lambda phi: f(phi).imag
    rhs_real = scipy.integrate.quad(f_real, -cm.pi, cm.pi)[0]
    rhs_imag = scipy.integrate.quad(f_imag, -cm.pi, cm.pi)[0]
    return 1 / (2 * cm.pi) * (rhs_real + 1j * rhs_imag)


def fourier_coeff(f: t.Callable[[float], complex]) -> t.Callable[[int], complex]:
    def _fcinstance(k):
        # The subdivision limit must be extended for larger k, because
        # trigonometric manipulation forces the rate of change to
        # go up.
        max_subdivisions = min((k + 1) * 50, 10000)
        integrand = lambda phi: f(phi) * cm.exp(-1j * k * phi)
        integrand_real = lambda phi: integrand(phi).real
        integrand_imag = lambda phi: integrand(phi).imag
        fk_real = scipy.integrate.quad(
            integrand_real, -cm.pi, cm.pi,
            limit=max_subdivisions)[0]
        fk_imag = scipy.integrate.quad(
            integrand_imag, -cm.pi, cm.pi,
            limit=max_subdivisions)[0]
        return 1/(2 * cm.pi) * (fk_real + 1j * fk_imag)
    return _fcinstance


def toeplitz(f, n) -> npt.NDArray:
    fk_inst = fourier_coeff(f)
    return scipy.linalg.toeplitz([fk_inst(i) for i in range(n)])


def eigsum_from_symbol(f: t.Callable[[float], complex], n: int) -> float:
    w, _ = np.linalg.eig(toeplitz(f, n))
    return 1/n * np.sum(w)


def eigsum_from_matrix(matrix: npt.NDArray) -> float:
    w, _ = np.linalg.eig(matrix)
    return 1/matrix.shape[0] * np.sum(w)