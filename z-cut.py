from numpy import *

import matplotlib.pyplot as plt

from scipy.fftpack import *

if __name__ == '__main__':
    lamb = 0.532e-6  # 波长
    k = 2 * pi / lamb  # 倾斜因子可以看做是常量
    L0 = 5e-3  # 衍射孔的尺寸
    z = 0.5 # 衍射孔到屏幕的距离
    f = 0.05

    row = 1080
    col = 1920
    U0 = zeros((row, col))  # 衍射孔光场分布
    # U0[int(row / 2 - row / 4): int(row / 2 + row / 4), int(col / 2 - col / 4): int(col / 2 + col / 4)] = 1
    # center = (row // 2, col // 2)  # 圆心
    # R = row // 4
    # r, c = ogrid[:row, :col]
    # bright = (c - center[1])**2 + (r - center[0])**2 <= R**2
    # U0[bright] = 1
    for r in range(row):
        for c in range(col):
            U0[r, c] = exp(1j * k * (c**2 + r**2) / 2 / f)
    
    x1 = linspace(-L0 / 2, L0 / 2, col)
    y1 = linspace(-L0 / 2, L0 / 2, row)
    x1, y1 = meshgrid(x1, y1)  # 构建网络

    Lr= row * lamb * z / L0
    Lc= col * lamb * z / L0
    x = linspace(-Lc / 2, Lc / 2, col)
    y = linspace(-Lr / 2, Lr / 2, row)
    x, y = meshgrid(x, y)

    F = U0 * exp(1j * k / 2 / z * (x1**2 + y1**2))
    F0 = fftshift(fft2(F))
    F1 = (exp(1j * k * z) / (1j * z * lamb)) * exp(1j * k / 2 / z * (x**2 + y**2))
    UP = F0 * F1
    plt.imshow(abs(U0),"gray")
    plt.show()



    
