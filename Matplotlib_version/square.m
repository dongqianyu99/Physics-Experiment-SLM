% 设置图像尺寸和孔的大小
N = 512;  % 图像尺寸
hole_size = 30;  % 方孔的大小（边长）

% 创建一个全黑的图像
image = zeros(N, N);

% 计算方孔的位置，确保方孔在图像中心
center = N / 2;  % 图像中心
half_hole_size = hole_size / 2;  % 方孔的一半大小

% 定义方孔的区域，设置为1（白色）
image(center - half_hole_size : center + half_hole_size - 1, center - half_hole_size : center + half_hole_size - 1) = 1;

% 显示图像
imshow(image);
title('图像中间的方孔');
colormap(gray);  % 使用灰度色图
axis equal;  % 保持纵横比
imwrite(image, 'square.png');