import numpy as np

import matplotlib.pyplot as plt
from gltseq.toeplitz import singsum_from_matrix


N = 100
eigsums_sr = np.empty(N-3)
eigsums_sn = np.empty(N-3)
eigsums_z = np.empty(N-3)
ns = np.arange(4, N+1)
for n in ns:
    R = np.zeros((n, n))
    N = np.diag(np.repeat(1/np.sqrt(n), n))
    R[0:1, 0:1] = 9
    eigsums_sr[n-4] = singsum_from_matrix(R)
    eigsums_sn[n-4] = singsum_from_matrix(N)
    eigsums_z[n-4] = singsum_from_matrix(R + N)
    

f = plt.figure()
ax: plt.Axes  = f.add_subplot(111)
# ax.set_title('Average Singular Values of Zero-Distributed Matrix')
ax.set_xlabel('$n$')
ax.set_ylabel(r'$\bar{\sigma}$')
ax.plot(ns, eigsums_sr, ns, eigsums_sn, '--', ns, eigsums_z, '.')
ax.legend([r'$R = [9]_{i,j=1}^2$', r'N = $\frac{1}{\sqrt{n}} I$', '$Z = R + N$'])
plt.show()
plt.close(f)
