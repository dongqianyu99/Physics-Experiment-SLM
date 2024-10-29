import numpy as np
import matplotlib.pyplot as plt

# 参数设置
N = 500
res = 1e-6
X = np.arange(-N/2, N/2)
Y = np.arange(-N/2, N/2)
x0, y0 = np.meshgrid(X * res, Y * res)
fx = np.arange(-1/(2*res), 1/(2*res), 1/(N*res))
fy = fx
fx, fy = np.meshgrid(fx, fy)
lam = 0.6328e-6
k = 2 * np.pi / lam
f0 = 5e-3
R = 1e-3
deltaf = 0
f = f0 + deltaf / R * np.sqrt(x0**2 + y0**2)

Ain = 1
Ein = Ain * np.exp(-1j * (np.pi / lam) * (np.sqrt(x0**2 + y0**2 + f0**2) - f0))
Nslid = 150
zd = 0.001 + np.linspace(0, 0.005, Nslid)
A1 = np.zeros((N, N, Nslid), dtype=complex)
Exy = np.zeros((N, N, Nslid))
Eyz = np.zeros((N, Nslid))

plt.figure(figsize=(10, 8))

for slid in range(Nslid):
    xout, yout = np.meshgrid(lam * zd[slid] * fx, lam * zd[slid] * fy)
    F0 = np.exp(1j * k * zd[slid]) / (1j * lam * zd[slid]) * np.exp(1j * k / (2 * zd[slid]) * (xout**2 + yout**2))
    F = np.exp(1j * np.pi / (lam * zd[slid]) * (x0**2 + y0**2))
    Exy[:, :, slid] = np.abs(F0 * np.fft.fftshift(np.fft.fft2(np.fft.fftshift(Ein * F))))
    Eyz[:, slid] = Exy[N//2, :, slid]

    # 绘制图像
    plt.subplot(2, 1, 1)
    plt.imshow(Exy[:, :, slid], extent=(xout[0, 0], xout[0, -1], yout[-1, 0], yout[0, 0]), cmap="jet", aspect='auto')
    plt.colorbar()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axis('equal')

    plt.subplot(2, 1, 2)
    plt.imshow(Eyz, extent=(zd[0], zd[-1], yout[-1, 0], yout[0, 0]), cmap="jet", aspect='auto')
    plt.colorbar()
    plt.xlabel('Z')
    plt.ylabel('Y')

    plt.pause(0.01)

plt.show()
