import numpy as np
import matplotlib.pyplot as plt

# 参数设置
wavelength = 532e-9  # 光的波长（单位：米）
focal_length = 0.1  # 透镜焦距（单位：米）
k = 2 * np.pi / wavelength  # 波数
size_x = 1980  # SLM分辨率
size_y = 1080
pixel_size = 8e-6  # SLM像素大小（单位：米）
n = 1.55

# 生成相位图
x = np.linspace(-size_x//2, size_x//2, size_x) * pixel_size
y = np.linspace(-size_y//2, size_y//2, size_y) * pixel_size
X, Y = np.meshgrid(x, y)
phase = (k * (n - 1) / (2 * focal_length)) * (X**2 + Y**2)  # 球透镜相位分布

# 将相位限制在 0 到 2π 之间
phase = np.mod(phase, 2 * np.pi)

# 可视化相位图
plt.imshow(phase, cmap='gray')
plt.colorbar()
plt.title('Phase Map of a Spherical Lens')
plt.show()

# 保存相位图为图片
plt.imsave('spherical_lens_phase_map.png', phase, cmap='gray')
