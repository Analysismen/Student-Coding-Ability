from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# 配置plt的figure文件，创建3d环境
fig = plt.figure()
ax = plt.axes(projection='3d')

# 三维线的数据
zline = np.linspace(0, 15, 1000)  # 0-15划分为1000等分
xline = np.sin(zline)
yline = np.cos(zline)
# xyz line 决定线，gray决定线颜色
ax.plot3D(xline, yline, zline, 'gray')
# 三维散点的数据
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
# 以xyz作为三个维度，c选择竖轴，cmap决定颜色
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Blues')
# 调整观察方向，前为俯仰角，后为方位角
ax.view_init(40, 60)
plt.show()

# from mpl_toolkits import mplot3d
# import numpy as np
# import matplotlib.pyplot as plt
#
# def f(x, y):
#     return np.sin(np.sqrt(x ** 2 + y ** 2))
#
# x = np.linspace(-6, 6, 30)
# y = np.linspace(-6, 6, 30)
# X, Y = np.meshgrid(x, y)
# # np.meshgrid生成高维坐标矩阵
# Z = f(X, Y)
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.contour3D(X, Y, Z, 50, cmap='Reds')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
# ax.view_init(60, 50)
#
# plt.show()
