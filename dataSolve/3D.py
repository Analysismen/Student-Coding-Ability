from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import dataSolve.MultiLinear3D as mul


# # 配置plt的figure文件，创建3d环境
# fig = plt.figure()
# ax = plt.axes(projection='3d')
#
# # 三维线的数据
# zline = np.linspace(0, 15, 1000)  # 0-15划分为1000等分
# xline = np.sin(zline)
# yline = np.cos(zline)
# # xyz line 决定线，gray决定线颜色
# ax.plot3D(xline, yline, zline, 'gray')
# # 三维散点的数据
# zdata = 15 * np.random.random(100)
# xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
# ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
# # 以xyz作为三个维度，c选择竖轴，cmap决定颜色
# ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Blues')
# # 调整观察方向，前为俯仰角，后为方位角
# ax.view_init(40, 60)
# plt.show()

def Visualization3D(valueArray):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    xline = np.linspace(0, 100, 10000)
    yline = np.linspace(0, 100, 10000)
    zline = xline * valueArray[1] + yline * valueArray[2] - valueArray[0]
    ax.plot3D(xline, yline, zline, 'black')

    outCome = np.array(mul.get_data())
    xdata = outCome[..., 1]
    ydata = outCome[..., 2]
    zdata = outCome[..., 0]

    # xdata = np.random.randn(100) * 30
    # ydata = xdata + np.random.randn(100) * 30
    # zdata = xdata * valueArray[1] + ydata * valueArray[2] - valueArray[0] + np.random.randn(100)*20
    ax.scatter3D(xdata, ydata, zdata, c=zdata)
    plt.show()
    plt.close()


if __name__ == "__main__":
    Visualization3D([-13.98, 2.088, 0.2257])
    outCome = mul.get_data()
    print(outCome[0])
