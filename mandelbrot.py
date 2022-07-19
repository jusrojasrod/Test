import numpy as np
import matplotlib.pyplot as plt
import time


def Mandel_func(z0, max_steps):
    z = 0j
    for itr in range(max_steps):
        if np.abs(z) > 2.0:
            return itr
        z = z * z + z0
    return max_steps


if __name__ == "__main__":

    Nx = 1000
    Ny = 1000
    max_steps = 100

    ext = [-2, 1, -1, 1]
    to = time.time()

    data = np.zeros([Nx, Ny])

    for i in range(Nx):
        for j in range(Ny):
            x = ext[0] + (ext[1] - ext[0]) * i / (Nx - i)
            y = ext[2] + (ext[3] - ext[2]) * i / (Ny - i)
            data[i, j] = Mandel_func(x + y * 1j, max_steps)
    print("clock time: " + str(time.time() - to))
    plt.imshow(np.transpose(1.0 / data), extent=ext)
    plt.show()
