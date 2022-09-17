from cmath import pi
from time import sleep
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as anim
from gltseq import specsym

N = 1000
_SYMBOL_RES = 10000
_BINS = 100
_STEPSIZE = 20

coeffs = [-1, 4, 2]
f = specsym.from_coeff(coeffs)

xs = np.linspace(-pi, pi, _SYMBOL_RES)
xs_symbol = [f(x) for x in xs]

fig, axs = plt.subplots(2)
fig.set_figwidth(10)
fig.set_figheight(10)
axs[0].hist(np.abs(xs_symbol), _BINS)
axs[0].set_title('Symbol (absolute sample)')
axs[0].set_xlabel('$s_i$')
axs[0].set_ylabel('count')

T = np.zeros((N, N))
for i, c in enumerate(coeffs):
    diag_i = i - len(coeffs) // 2
    T += np.diag(np.repeat(c, N - abs(diag_i)), diag_i)
_, xs_sings, _= np.linalg.svd(T)
axs[1].hist(xs_sings, _BINS, color='forestgreen')
axs[1].set_title('Singular Values')
axs[1].set_xlabel('$\sigma_i$')
axs[1].set_ylabel('count')

plt.show()
fig.tight_layout()
fig.savefig("media/distribution.png", dpi=600)
