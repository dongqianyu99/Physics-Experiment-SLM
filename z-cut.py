from numpy import *

import matplotlib.pyplot as plt

from scipy.fftpack import *

if __name__ == '__main__':
    raw = 1920
    col = 1080
    U0 = zeros((raw, col))  # 衍射孔光场分布
    U0[int(raw / 2 - raw / 4): int(raw / 2 + raw / 4), int(col / 2 - col / 4): int(col / 2 + col / 4)] = 1
    
    lamb = 0.6328e-6  # 波长
    k = 2 * pi / lamb  # 倾斜因子可以看做是常量
    L0 = 5e-3  # 衍射孔的尺寸
    z = 0.05 # 衍射孔到屏幕的距离
    
    x0 = linspace(-L0 / 2, L0 / 2, col)
    y0 = linspace(-L0 / 2, L0 / 2, raw)
    x0, y0 = meshgrid(x0, y0)  # 构建网络




    
