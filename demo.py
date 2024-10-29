from numpy import *

import matplotlib.pyplot as plt

from scipy.fftpack import *

if __name__ == '__main__':
    r=1080
    c=1920
    a=zeros((r,c))
    a[int(r/2-r/4):int(r/2+r/4),int(c/2-c/4):int(c/2+c/4)]=1
    lamb=0.6328e-6  # 波长，用米表示
    k=2*pi/lamb
    L0=5e-3
    d=0.05  # 缝隙到屏幕的距离

    x0=linspace(-L0/2,L0/2,c)
    y0=linspace(-L0/2,L0/2,r)
    x0,y0=meshgrid(x0,y0)  # 构建网格
    L=r*lamb*d/L0  # 
    x1=linspace(-L/2,L/2,c)
    y1 = linspace(-L / 2, L / 2, r)
    x1,y1=meshgrid(x1,y1)
    F0=exp(1j*k*d)/(1j*lamb*d)*exp(1j*k/2/d*(x1**2+y1**2))
    F=exp(1j*k/2/d*(x0**2+y0**2))
    a=a*F
    F=fftshift(fft2(a))
    F_feild=F0*F
    plt.imshow(abs(F_feild),"gray")
    plt.show()