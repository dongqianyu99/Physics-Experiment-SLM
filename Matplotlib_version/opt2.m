N = 1024;
i = imread("square.png");
lev = graythresh(i);
u = im2bw(i, lev);
%subplot(2,2,1),imshow(u);
lam = 500e-4;
k = 2*pi/lam;
z = 400000;
z1 = 300000;
a0 = 3000000;
x2 = 0: 1: 1023;
y2 = 0: 1: 1023;
for i = 1: 1: 1024
    for j = 1: 1: 1024
        r(i, j) = sqrt((x2(i) - 512)^2 + (y2(j) - 512)^2 + z1^2);
        U1(i, j) = a0/r(i, j) * exp((-1)^(1/2) * k * r(i, j));
    end
end
u1 = U1.*u;

[x, y] = meshgrid(linspace(-N, N, N));
U = fftshift(fft2(u1));
h = exp(1j * k * z) * exp((1j * k *(x.^2 + y.^2)) / (2 * z)) / (1j * lam * z);
H = fftshift(fft2(h));
A = fftshift(ifft2(H.*U));
axis image;
colormap("hot")
I = abs(A);
%imshow(I);
%mesh(I);
plot(x(1, :), I(521, :))
% subplot(2,2,2), imshow(I);
% colormap("hot")
% subplot(2,2,3), mesh(I);
% subplot(2,2,4), plot(x(1, :), I(521, :));
