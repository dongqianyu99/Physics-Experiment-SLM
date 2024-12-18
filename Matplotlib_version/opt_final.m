ROW = 1080;
COL = 1920;
i = imread("2.png");
%lev = graythresh(i);
gray_image = im2gray(i); 
u = mat2gray(gray_image);
imshow(u);
disp(size(gray_image));

lam = 532e-9;
k = 2 * pi / lam;
z = 0.4;
z1 = 0.4;
a0 = 0.2;
for i = 1: 1: 1080
    for j = 1: 1: 1920
        U1(i, j) = a0 * exp((-1)^(1 / 2) * k * z1);
    end
end
u1 = U1.*u;
%disp(size(u1));

