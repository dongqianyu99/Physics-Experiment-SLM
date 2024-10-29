from numpy import *

import matplotlib.pyplot as plt

from scipy.fftpack import *

if __name__ == '__main__':
    r=1080
    c=1920
    a=zeros((r,c))

    # 创建一个圆形区域
    center = (r // 2, c // 2)  # 圆心
    radius = r // 4  # 半径
    Y, X = ogrid[:r, :c]
    mask = (X - center[1])**2 + (Y - center[0])**2 <= radius**2
    a[mask] = 1  # 设置圆形区域为1

    # a[int(r/2-r/4):int(r/2+r/4),int(c/2-c/4):int(c/2+c/4)]=1
    lamb=0.6328e-6  # 波长，用米表示
    k=2*pi/lamb
    L0=5e-3
    d=0.05  # 缝隙到屏幕的距离



    x0=linspace(-L0/2,L0/2,c)
    y0=linspace(-L0/2,L0/2,r)
    x0,y0=meshgrid(x0,y0)  # 构建网格
    Lr=r*lamb*d/L0  # 
    Lc=c*lamb*d/L0
    x1=linspace(-Lc/2,Lc/2,c)
    y1 = linspace(-Lr / 2, Lr / 2, r)
    x1,y1=meshgrid(x1,y1)
    F0=exp(1j*k*d)/(1j*lamb*d)*exp(1j*k/2/d*(x1**2+y1**2))
    F=exp(1j*k/2/d*(x0**2+y0**2))
    a=a*F
    F=fftshift(fft2(a))
    F_feild=F0*F
    plt.imshow(abs(F_feild),"gray")
    plt.show()