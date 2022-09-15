import numpy as np

import matplotlib.pyplot as plt
from gltseq.toeplitz import eigsum_from_matrix


N = 100
MIN_N = 2
eigsums_a = np.empty(N-MIN_N+1)
eigsums_b = np.empty(N-MIN_N+1)
eigsums_z = np.empty(N-MIN_N+1)
eigdiffs_ab = np.empty(N-MIN_N+1)
ns = np.arange(MIN_N, N+1)
for n in ns:
    B = \
        np.diag(np.repeat(3, n)) \
        + np.diag(np.repeat(1, n-1), 1) \
        + np.diag(np.repeat(1, n-1), -1)
    R = np.zeros((n, n))
    N = np.full((n, n), 1/n)
    A = B + R + N
    R[0:1, 0:1] = 9
    eigsums_a[n-MIN_N] = eigsum_from_matrix(A)
    eigsums_b[n-MIN_N] = eigsum_from_matrix(B)
    eigsums_z[n-MIN_N] = eigsum_from_matrix(R + N)
    eigdiffs_ab[n-MIN_N] = np.average(np.linalg.eig(A)[0] - np.linalg.eig(B)[0])

f = plt.figure()
ax: plt.Axes  = f.add_subplot(111)
ax.set_title('Average Eigenvalues of Disturbed Matrix')
ax.set_xlabel('$n$')
ax.set_ylabel(r'$\bar{\lambda}$')
ax.plot(ns, eigsums_a, '--', ns, eigsums_b, '.', ns, eigsums_z, '.', ns, eigdiffs_ab)
ax.legend([r'$A = B+Z$', r'$B = toeplitz(1, 3, 1)$', '$Z = R + N$', 'ev diff of A, B'])
ax.set_xlim(0)
ax.set_ylim(0)
plt.show()
plt.close(f)
