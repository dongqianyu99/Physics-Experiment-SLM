import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import *

# 参数设置
lam = 0.6328e-6  # 波长
k = 2 * np.pi / lam
f = 5e-3  # 焦距
res = 1e-6  # 分辨率
N = 500  # 网格大小

# 衍射距离 (指定值，例如 0.002)
z = 0.002

# 创建空间网格和频域网格
x0 = np.linspace(-N / 2, N / 2, N) * res
y0 = np.linspace(-N / 2, N / 2, N) * res
x0, y0 = np.meshgrid(x0, y0)

fx = fftfreq(N, res)  # 频率坐标
fy = fx
xout, yout = np.meshgrid(lam * z * fx, lam * z * fy)

# 初始电场波前 (例如，平面波)
Ein = np.exp(-1j * (np.pi / lam) * ((x0**2 + y0**2) / f))

# 计算传播因子
F0 = np.exp(1j * k * z) / (1j * lam * z) * np.exp(1j * k / 2 / z * (xout**2 + yout**2))
F = np.exp(1j * np.pi / (lam * z) * (x0**2 + y0**2))

# 计算衍射场
Exy = np.abs(F0 * fftshift(fft2(fftshift(Ein * F))))

# 提取沿 y 方向的电场强度
Eyz = Exy[N // 2, :]

# 绘制图像
plt.figure(figsize=(8, 6))

# 绘制 Exy 场
plt.subplot(2, 1, 1)
plt.imshow(Exy, aspect='auto', cmap='jet', extent=[xout[0, 0], xout[0, -1], yout[0, 0], yout[-1, 0]])
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar()
plt.title('Exy Field')

# 绘制 Eyz 场
plt.subplot(2, 1, 2)
plt.plot(yout[N // 2, :], Eyz, color='gray')
plt.xlabel('Y')
plt.ylabel('Eyz')
plt.title('Eyz Field')

# 显示图像
plt.tight_layout()
plt.show()
