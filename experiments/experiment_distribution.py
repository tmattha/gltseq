from cmath import pi
import enum
from time import sleep
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as anim
from gltseq import toeplitz, specsym

N = 1000
_SYMBOL_RES = 10000
_BINS = 100
_STEPSIZE = 20

coeffs = [-1, 4, 2]
f = specsym.from_coeff(coeffs)

xs = np.linspace(-pi, pi, _SYMBOL_RES)
xs_symbol = [f(x) for x in xs]

fig, axs = plt.subplots(2)
fig.set_figwidth(4)
fig.set_figheight(8)
axs[0].hist(np.abs(xs_symbol), _BINS)
axs[0].set_title('Symbol (absolute)')
axs[1].set_title('Singular Values')

def update(frame):
    # T = toeplitz.toeplitz(f, frame)
    T = np.zeros((frame, frame))
    for i, c in enumerate(coeffs):
        diag_i = i - len(coeffs) // 2
        T += np.diag(np.repeat(c, frame - abs(diag_i)), diag_i)
    _, xs_eigs, _= np.linalg.svd(T)

    
    return axs[1].hist(xs_eigs, _BINS, color='forestgreen')[2].patches

ani = anim.FuncAnimation(fig, update, frames=range(5, N, _STEPSIZE), blit=True)
ani.save('distribution_converge.mp4', fps=3, dpi=300)
# plt.show()
