import numpy as np
import matplotlib.pyplot as plt

# Snell's law: n1 * sin(theta1) = n2 * sin(theta2)
def snell_law(n1, n2, theta1):
    return np.arcsin(n1 / n2 * np.sin(theta1))

# 求球面与光线的交点
def intersection_point(ray_origin, ray_direction, sphere_center, sphere_radius):
    oc = ray_origin - sphere_center
    a = np.dot(ray_direction, ray_direction)
    b = 2.0 * np.dot(oc, ray_direction)
    c = np.dot(oc, oc) - sphere_radius**2
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # No intersection
    t = (-b - np.sqrt(discriminant)) / (2.0 * a)
    return ray_origin + t * ray_direction

# 计算法线
def normal_at_surface(point, sphere_center):
    return (point - sphere_center) / np.linalg.norm(point - sphere_center)

# 定义球面透镜的参数
n_air = 1.0       # 空气折射率
n_glass = 1.5     # 玻璃折射率
radius1 = 10.0    # 第一个球面曲率半径
radius2 = -10.0   # 第二个球面曲率半径（负号表示凹面）
thickness = 5.0   # 透镜厚度

# 定义透镜的位置
lens_center1 = np.array([0, 0, 0])                   # 第一表面的球心
lens_center2 = np.array([0, 0, thickness + radius2]) # 第二表面的球心

# 初始光线参数
ray_origin = np.array([0, 0, -20])  # 光线起点
ray_direction = np.array([0, 0, 1]) # 光线方向，平行于光轴

# 与第一个表面的交点
intersection1 = intersection_point(ray_origin, ray_direction, lens_center1, radius1)
if intersection1 is None:
    print("No intersection with the first surface")
else:
    # 计算法线并根据Snell定律计算折射
    normal1 = normal_at_surface(intersection1, lens_center1)
    theta1 = np.arccos(np.dot(-ray_direction, normal1))  # 入射角
    theta2 = snell_law(n_air, n_glass, theta1)           # 折射角

    # 计算折射后的方向
    refracted_direction1 = ray_direction * np.cos(theta2) + normal1 * np.sin(theta2)

    # 与第二表面的交点
    intersection2 = intersection_point(intersection1, refracted_direction1, lens_center2, radius2)
    if intersection2 is None:
        print("No intersection with the second surface")
    else:
        # 计算法线并计算光线从玻璃到空气的折射
        normal2 = normal_at_surface(intersection2, lens_center2)
        theta3 = np.arccos(np.dot(-refracted_direction1, normal2))  # 入射角
        theta4 = snell_law(n_glass, n_air, theta3)                  # 折射角

        # 计算折射后的方向
        refracted_direction2 = refracted_direction1 * np.cos(theta4) + normal2 * np.sin(theta4)

        # 打印结果
        print(f"First intersection: {intersection1}")
        print(f"Second intersection: {intersection2}")
        print(f"Final ray direction after lens: {refracted_direction2}")

# 可视化光线和透镜
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制透镜的两个球面
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x1 = radius1 * np.cos(u) * np.sin(v)
y1 = radius1 * np.sin(u) * np.sin(v)
z1 = radius1 * np.cos(v)
ax.plot_surface(x1, y1, z1 - radius1, color="b", alpha=0.3)

x2 = radius2 * np.cos(u) * np.sin(v)
y2 = radius2 * np.sin(u) * np.sin(v)
z2 = radius2 * np.cos(v)
ax.plot_surface(x2, y2, z2 + thickness, color="r", alpha=0.3)

# 绘制光线
ax.plot([ray_origin[0], intersection1[0]], [ray_origin[1], intersection1[1]], [ray_origin[2], intersection1[2]], color="g")
ax.plot([intersection1[0], intersection2[0]], [intersection1[1], intersection2[1]], [intersection1[2], intersection2[2]], color="g")

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
