from numpy import *

import matplotlib.pyplot as plt

from scipy.fftpack import *

if __name__ == '__main__':
    lamb = 0.532e-6  # 波长
    k = 2 * pi / lamb  # 倾斜因子可以看做是常量
    L0 = 5e-3  # 衍射孔的尺寸
    L1 = 450e-5
    L2 = 800e-5
    z = 0.5  # 衍射孔到屏幕的距离
    f = 0.5
    px, py = 8e-6, 8e-6  # 每个像素的物理尺寸，单位为米

    row = 1080
    col = 1920
    U0 = zeros((row, col))  # 衍射孔光场分布
    # U0[int(row / 2 - row / 4): int(row / 2 + row / 4), int(col / 2 - col / 4): int(col / 2 + col / 4)] = 1
    center = (row // 2, col // 2)  # 圆心
    R = row // 4
    r, c = ogrid[:row, :col]
    bright = (c - center[1])**2 + (r - center[0])**2 <= R**2
    U0[bright] = 1

    # x1 = linspace(-col/2, col/2, col) * px
    # y1 = linspace(-row/2, row/2, row) * py
    # x1, y1 = meshgrid(x1, y1)
    # # 计算球透镜的相位分布
    # U0 = k * (x1**2 + y1**2) / (2 * f)
    # U0 = mod(U0, 2 * pi)

    x1 = linspace(-L2 / 2, L2 / 2, col)
    y1 = linspace(-L1 / 2, L1 / 2, row)
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
    plt.imshow(abs(UP),"gray")
    plt.show()



    
