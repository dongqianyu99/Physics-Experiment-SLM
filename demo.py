import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import *

# 定义常数
lamb = 0.532e-6  # 波长 (单位：米)
k = 2 * np.pi / lamb  # 波数
z = 0.5  # 衍射距离 (单位：米)
f = 0.5
L = 5e-3  # 计算区域的尺寸 (单位：米)
col, row = 512, 512  # 网格分辨率
px, py = L / col, L / row  # 每个像素的尺寸 (单位：米)

# 创建空间坐标网格
x = np.linspace(-L / 2, L / 2, col)
y = np.linspace(-L / 2, L / 2, row)
x, y = np.meshgrid(x, y)

# 初始波前 U0
U0 = np.exp(1j * k * (x**2 + y**2) / (2 * f))  # 初始相位场

L0 = row * lamb * z / L

x1 = np.linspace(-L0 / 2, L0 / 2, col)
y1 = np.linspace(-L0 / 2, L0 / 2, row)
x1, y1 = np.meshgrid(x1, y1)

F = U0 * np.exp(1j * k / 2 / z * (x**2 + y**2))
F0 = fftshift(fft2(F))
F1 = (np.exp(1j * k * z) / (1j * z * lamb)) * np.exp(1j * k / 2 / z * (x1**2 + y1**2))
U1 = F0 * F1
# plt.imshow(abs(UP),"gray")
# plt.show()
plt.imshow(np.abs(U1), cmap='gray')
plt.colorbar()
plt.title('Fresnel Diffraction')
plt.show()




# # 频域坐标（通过 FFT 转换后的频率）
# fx = np.fft.fftfreq(col, px)
# fy = np.fft.fftfreq(row, py)
# fx, fy = np.meshgrid(fx, fy)

# # 菲涅尔衍射的相位因子
# H = np.exp(1j * np.pi * lamb * z * (fx**2 + fy**2))

# # 计算傅里叶变换并加上相位因子
# U0_fft = np.fft.fftshift(np.fft.fft2(U0))  # 傅里叶变换
# U1_fft = U0_fft * H  # 在频域中乘上相位因子

# # 反傅里叶变换得到衍射场
# U1 = np.fft.ifft2(np.fft.ifftshift(U1_fft))

# # 可视化结果
# plt.imshow(np.abs(U1), cmap='gray')
# plt.colorbar()
# plt.title('Fresnel Diffraction')
# plt.show()