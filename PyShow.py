import numpy as np
import matplotlib.pyplot as plt
import component.FirstGit as first

a = []
b = []
dict0 = first.getDictFirstGit()
for key,value in dict0.items():
    a.append(key)
    b.append(value)
x = np.asarray(a)
y = np.asarray(b)
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
# # x轴，y轴展示
# plt.plot(x,y)
# plt.show()
# # 散点图
# plt.plot(x,y,'ob')
# plt.show()
# #柱状图
# x2 = x
# y2 = y
# plt.bar(x, y, align =  'center')
# plt.bar(x2, y2, color =  'g', align =  'center')
# plt.title('Bar graph')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
# plt.show()