import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import *

# 参数设置
lam = 0.532e-6  # 波长
k = 2 * np.pi / lam
N = 500  # 网格大小
f = 5e-3  # 焦距
res = 1e-6  # 分辨率
zd = 0.001 + np.linspace(0, 0.005, 50)  # 衍射距离
Nslid = 50  # 滑动层数

# 初始化网格和场
x0 = np.linspace(-N/2, N/2, N) * res
y0 = np.linspace(-N/2, N/2, N) * res
x0, y0 = np.meshgrid(x0, y0)

fx = np.fft.fftfreq(N, res)  # 频率坐标
fy = fx
xout, yout = np.meshgrid(lam * zd[0] * fx, lam * zd[0] * fy)

# 初始化场和结果存储
Ein = np.exp(-1j * (np.pi / lam) * ((x0**2 + y0**2) / f))
Exy = np.zeros((N, N, Nslid), dtype=complex)
Eyz = np.zeros((N, Nslid))

# 绘图
plt.figure(figsize=(8, 6))

for slid in range(Nslid):
    # 计算频域传播因子
    xout, yout = np.meshgrid(lam * zd[slid] * fx, lam * zd[slid] * fy)
    F0 = np.exp(1j * k * zd[slid]) / (1j * lam * zd[slid]) * np.exp(1j * k / 2 / zd[slid] * (xout**2 + yout**2))
    F = np.exp(1j * np.pi / (lam * zd[slid]) * (x0**2 + y0**2))

    # 计算场
    Exy[:, :, slid] = np.abs(F0 * fftshift(fft2(fftshift(Ein * F))))

    # 取出特定行的电场强度
    Eyz[:, slid] = Exy[N//2, :, slid]

    # 绘制图像
    plt.subplot(2, 1, 1)
    plt.imshow(np.abs(Exy[:, :, slid]), aspect='auto', cmap='jet', extent=[xout[0, 0], xout[0, -1], yout[0, 0], yout[-1, 0]])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.colorbar()
    plt.title('Exy Field')

    plt.subplot(2, 1, 2)
    plt.imshow(np.abs(Eyz), aspect='auto', cmap='jet', extent=[zd[0], zd[-1], yout[0, 0], yout[-1, 0]])
    plt.xlabel('Z')
    plt.ylabel('Y')
    plt.colorbar()
    plt.title('Eyz Field')

    plt.pause(0.001)  # 用来模拟 MATLAB 中的 pause(eps)，让图像实时更新

plt.show()
