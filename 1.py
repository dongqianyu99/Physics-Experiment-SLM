import numpy as np
import matplotlib.pyplot as plt

# 参数设置
M, N = 1920, 1080 # SLM的分辨率（1920x1080）
focal_length = 0.1 # 二次曲面透镜的焦距（可以根据需要调整）
wavelength = 532e-9 # 波长（单位为米），53纳米
pixel_size = 8e-6  # SLM像素大小（单位：米）

# 生成坐标网格
x = np.linspace(-M // 2, M // 2, N) * pixel_size
y = np.linspace(-N // 2, N // 2, N) * pixel_size
X, Y = np.meshgrid(x, y)

# 计算球透镜的相位分布
R_squared = X**2 + Y**2
k = 2 * np.pi / wavelength # 波数
phase_lens = (k * 0.55 / (2 * focal_length)) * R_squared

# 将相位映射到0到2π之间
phase_lens = np.mod(phase_lens, 2 * np.pi)

# 保存相位图像，保存在代码所在文件夹
plt.imsave("sphere_lens_phase_1920x1080.png", phase_lens, cmap='gray')