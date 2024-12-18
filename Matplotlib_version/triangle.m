% 创建一个512x512的黑色背景图像
N = 512;  % 图像的尺寸
image = zeros(N, N);  % 初始化图像为全零（黑色）

% 定义三角形的三个顶点坐标
x = [N/2 - 30, N/2, N/2 + 30];  % 三角形的x坐标
y = [N/2 + 30, N/2 - 30, N/2 + 30];  % 三角形的y坐标

% 使用poly2mask函数生成三角形区域的掩膜
mask = poly2mask(x, y, N, N);

% 将掩膜应用到图像中，三角形区域设为白色（值为255）
image(mask) = 1;  % 设定三角形区域为白色（255）

% 显示图像
imshow(image);
%title('512x512 灰度图 中间的三角形衍射孔');
colormap(gray);  % 使用灰度色图
axis equal;
imwrite(image, 'triangle_aperture.png');