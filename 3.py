import numpy as np
from PIL import Image

# 定义光学参数
wavelength = 532e-9  # 波长，例如绿光532nm
focal_length = 0.5   # 焦距，单位为米
a = 1e-6  # 二次曲面的系数
b = 1e-12  # 三次曲面的系数

# SLM 参数
Nx, Ny = 1920, 1080   # SLM 的分辨率
px, py = 10e-6, 10e-6 # 每个像素的物理尺寸，单位为米

# 计算网格坐标
x = np.linspace(-Nx/2, Nx/2, Nx) * px
y = np.linspace(-Ny/2, Ny/2, Ny) * py
X, Y = np.meshgrid(x, y)

# 计算球透镜的相位分布
phase_spherical = (2 * np.pi / wavelength) * (X**2 + Y**2) / (2 * focal_length)

# 计算二次曲面透镜的相位分布
phase_quadratic = (2 * np.pi / wavelength) * a * (X**2 + Y**2)

# 计算三次曲面透镜的相位分布
phase_cubic = (2 * np.pi / wavelength) * b * (X**3 + Y**3)

# 将相位限制在 0 到 2π 之间
phase_spherical_mod = np.mod(phase_spherical, 2 * np.pi)
phase_quadratic_mod = np.mod(phase_quadratic, 2 * np.pi)
phase_cubic_mod = np.mod(phase_cubic, 2 * np.pi)

# 将相位值转换为8-bit灰度值
def phase_to_grayscale(phase):
    return (phase / (2 * np.pi) * 255).astype(np.uint8)

# 保存相位图像
Image.fromarray(phase_to_grayscale(phase_spherical_mod)).save('spherical_lens_phase.png')
Image.fromarray(phase_to_grayscale(phase_quadratic_mod)).save('quadratic_lens_phase.png')
Image.fromarray(phase_to_grayscale(phase_cubic_mod)).save('cubic_lens_phase.png')

print("相位图已生成并保存为图片。")