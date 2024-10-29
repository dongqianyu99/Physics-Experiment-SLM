import numpy as np
import matplotlib.pyplot as plt

def plot_ellipse(eccentricity):
    # 定义椭圆的参数
    a = 1  # 半长轴
    if eccentricity<1 :
        b = np.sqrt(1 - eccentricity**2)  # 半短轴
    else: 
        b = np.sqrt(eccentricity**2 - 1)

    # 生成角度
    theta = np.linspace(0, 2 * np.pi, 100)

    # 计算椭圆的坐标
    x = a * np.cos(theta)
    y = b * np.sin(theta)

    # 绘制椭圆
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label=f'Eccentricity = {eccentricity}')
    plt.title('Ellipse with Given Eccentricity')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axhline(0, color='gray', lw=0.5, ls='--')
    plt.axvline(0, color='gray', lw=0.5, ls='--')
    plt.legend()
    plt.grid()
    plt.show()

# 调用函数，绘制离心率为0.5的椭圆
plot_ellipse(2)