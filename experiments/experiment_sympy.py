import sympy
import scipy.linalg


sympy.init_printing(use_unicode=True)

theta = sympy.Symbol('theta')
k = sympy.Symbol('k')
n = sympy.Integer(6)
f = sympy.Symbol('f')
f_fd = 2 - 2 * sympy.cos(theta)
rhs: sympy.core.numbers.Integer = 1/(2 * sympy.pi) * sympy.Integral(f, (theta, -sympy.pi, sympy.pi))

print(rhs.subs(f, f_fd).doit())

integrand = f * sympy.exp(-1j * k * theta)
fk = 1/(2 * sympy.pi) * sympy.Integral(integrand, (theta, -sympy.pi, sympy.pi))

fk_fd = fk.subs(f, f_fd).doit()
T_fd = sympy.Matrix(scipy.linalg.toeplitz([fk_fd.subs(k, sympy.Integer(i).doit()) for i in range(n)]))
lhs = 1/n * sympy.ones(1, n) * sympy.Matrix(list(T_fd.eigenvals().keys()))
print(lhs)