% 参数设置
N = 1024;  % 图像大小
lambda = 532e-9;  % 波长（532 nm, 绿色光）
k = 2 * pi / lambda;  % 波数
f = 0.5;  % 焦距（假设为1000单位）
z = 0;  % 透镜的中心位置
[x, y] = meshgrid(linspace(-N, N, N));  % 生成坐标网格

% 计算球透镜相位
r2 = x.^2 + y.^2;  % 半径平方
phi = exp(1i * k / (2 * f) * r2);  % 球透镜的相位变化

% 显示结果
imagesc(angle(phi));  % 显示相位图像
colormap("gray");  % 设置颜色映射
axis image;  % 保持纵横比

