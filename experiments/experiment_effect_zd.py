import numpy as np

import matplotlib.pyplot as plt
from gltseq.toeplitz import singsum_from_matrix


N = 100
MIN_N = 2
singsums_a = np.empty(N-MIN_N+1)
singsums_b = np.empty(N-MIN_N+1)
singsums_z = np.empty(N-MIN_N+1)
singdiffs_ab = np.empty(N-MIN_N+1)
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
    singsums_a[n-MIN_N] = singsum_from_matrix(A)
    singsums_b[n-MIN_N] = singsum_from_matrix(B)
    singsums_z[n-MIN_N] = singsum_from_matrix(R + N)
    singdiffs_ab[n-MIN_N] = np.average(np.linalg.svd(A)[1] - np.linalg.svd(B)[1])

f = plt.figure()
ax: plt.Axes  = f.add_subplot(111)
#ax.set_title('Average Singular Values of Perturbed Matrix')
ax.set_xlabel('$n$')
ax.set_ylabel(r'$\bar{\sigma}$')
ax.plot(ns, singsums_a, '--', ns, singsums_b, '.', ns, singsums_z, '.', ns, singdiffs_ab)
ax.legend([r'$A = B+Z$', r'$B = toeplitz(1, 3, 1)$', '$Z = R + N$', 'sv diff of A, B'])
ax.set_xlim(0)
ax.set_ylim(0)
plt.show()
f.savefig("media/effect_zd.png", dpi=600)
