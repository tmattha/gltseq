from cmath import pi
import enum
from time import sleep
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as anim
from gltseq import toeplitz, specsym

N = 1000
_SYMBOL_RES = 10000
_BINS = 30
_STEPSIZE = 20

coeff = [2, -1, 4, 2, -1]
f = specsym.from_coeff([2, -1, 4, 2, -1])
# T = toeplitz.toeplitz(f, N)


xs = np.linspace(-pi, pi, _SYMBOL_RES)
xs_symbol = [f(x) for x in xs]
# xs_eigs, _ = np.linalg.eig(T)

fig, axs = plt.subplots(2, 2)
fig.set_figwidth(4)
fig.set_figheight(3)
axs[0][0].hist(np.real(xs_symbol), _BINS)
axs[0][0].set_title('Symbol (real)')
axs[0][1].hist(np.imag(xs_symbol), _BINS)
axs[0][1].set_title('Symbol (imaginary)')
axs[1][0].set_title('Eigenvalues (real)')
axs[1][1].set_title('Eigenvalues (imaginary)')


def init():
    ln1, = axs[1][0].eventplot([])
    ln2, = axs[1][1].eventplot([])
    return [ln1, ln2]

def update(frame):
    # T = toeplitz.toeplitz(f, frame)
    T = np.zeros((frame, frame))
    for i, c in enumerate(coeff):
        diag_i = i - len(coeff) // 2
        T += np.diag(np.repeat(c, frame - abs(diag_i)), diag_i)
    xs_eigs, _ = np.linalg.eig(T)
    artists = []
    artists.extend(
        axs[1][0].hist(
            np.real(xs_eigs), _BINS, color='forestgreen'
            )[2].patches)
    artists.extend(
        axs[1][1].hist(
            np.imag(xs_eigs), _BINS, color='forestgreen'
            )[2].patches)
    return artists

ani = anim.FuncAnimation(fig, update, frames=range(5, N, _STEPSIZE),
    init_func=init, blit=True)
ani.save('distribution_converge.mp4', fps=3, dpi=300)
# plt.show()
