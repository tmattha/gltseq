import cmath as cm


def fd_diffusion(phi):
    return 2 - 2 * cm.cos(phi)


def diag(d):
    return lambda _: d