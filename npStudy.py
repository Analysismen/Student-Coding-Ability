import numpy as np

# # 数据类型，输出结果为 int32
# dt = np.dtype(np.int32)
# print(dt)
#
# # int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
# # 输出结果为 int32
# dt = np.dtype('i4')
# print(dt)
#
# # 字节顺序标注
# # 输出结果为 int32
# dt = np.dtype('<i4')
# print(dt)

# # 类型字段名可以用于存取实际的 age 列
# # 输出结果为 [10 20 30]
# dt = np.dtype([('age',np.int8)])
# a = np.array([(10,),(20,),(30,)], dtype = dt)
# print(a['age'])
#
# student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
# print(student.itemsize)
#
# # ndim 返回维度
# a = np.arange(24)
# print(a.ndim)             # a 现只有一个维度
# print(a.shape)
# # 现在调整其大小
# b = a.reshape(2,4,3)  # b 现在拥有三个维度
# print(b.ndim)
# print(b.shape)
# # print(b)
# b.shape = (4,2,3)
# # print(b)
# print(b.itemsize)
# print(b.flags)

# # zeros
# # 默认为浮点数
# x = np.zeros(5)
# print(x)
# # 设置类型为整数
# y = np.zeros((5,), dtype=np.int)
# print(y)
# # 自定义类型
# z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
# print(z)

# # ones
# # 默认为浮点数
# x = np.ones(5)
# print(x)
# # 自定义类型
# x = np.ones([2, 2], dtype=int)
# print(x)

# # 将列表转换成asarray
# x = [1,2,3]
# a = np.asarray(x)
# print(a)
#
# # 将元组转换成asarray
# x = [(1, 2, 3), (4, 5)]
# b = np.asarray(x,dtype='object')
# print(b)

# 切分引索
# a = np.arange(10)
# b = a[2:7:2]   # 从索引 2 开始到索引 7 停止，间隔为 2
# print(b)
# s = slice(2,7,2)   # 从索引 2 开始到索引 7 停止，间隔为2
# print(a[s])

# 引索方面 ： 的详细用法
# a = np.arange(10)
# print(a[2])
# print(a[2:])
# print(a[2:5])

# # 高维的提取
# a = np.array([[1,2,3],[3,4,5],[4,5,6]])
# print(a)
# # 从某个索引处开始切割
# print('从数组索引 a[1:] 处开始切割')
# print(a[1:])
#
# # 切片还可以包括省略号 …，来使选择元组的长度与数组的维度相同。 如果在行位置使用省略号，它将返回包含行中元素的 ndarray
# a = np.array([[1,2,3],[3,4,5],[4,5,6]])
# print (a[...,1])   # 第2列元素
# print (a[1,...])   # 第2行元素
# print (a[...,1:])  # 第2列及剩下的所有元素

# # 获取数组中(0,0)，(1,1)和(2,0)位置处的元素
# # x = np.array([[1,  2],  [3,  4],  [5,  6]])
# # y = x[[0,1,2],  [0,1,0]]
# # print (y)
# #
# # x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
# # print ('我们的数组是：' )
# # print (x)
# # print ('\n')
# # rows = np.array([[0,0],[3,3]])
# # cols = np.array([[0,2],[0,2]])
# # y = x[rows,cols]
# # print  ('这个数组的四个角元素是：')
# # print (y)
# #
# # # 借助 ： 和 …… 进行切片
# # a = np.array([[1,2,3], [4,5,6],[7,8,9]])
# # b = a[1:3, 1:3]
# # c = a[1:3,[0]]
# # d = a[...,1:]
# # print(b)
# # print(c)
# # print(d)
# #
# # # 通过布尔进行计算
# # x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
# # print('我们的数组是：')
# # print(x)
# # print('\n')
# # # 现在我们会打印出大于 5 的元素
# # print('大于 5 的元素是：')
# # print(x[x>5])

# # 以下实例使用了 ~（取补运算符）来过滤 NaN。
# a = np.array([np.nan,  1,2,np.nan,3,4,5])
# print (a[~np.isnan(a)])
#
# # 过滤掉非复数元素
# a = np.array([1,  2+6j,  5,  3.5+5j])
# print (a[np.iscomplex(a)])

# # 奇怪的花式引索 看不懂了
# x=np.arange(32).reshape((8,4))
# print (x[[4,2,1,7]])
# print (x[[-4,-2,-1,-7]])
# # 传入多个索引数组（要使用np.ix_）
# print (x[np.ix_([1,5,7,2],[0,3,1,2])])

# # 广播 对应位运算
# #  a.shape == b.shape，那么 a*b 的结果就是 a 与 b 数组对应位相乘
# a = np.array([1,2,3,4])
# b = np.array([10,20,30,40])
# c = a * b
# print(c)
#
# # 当运算中的 2 个数组的形状不同时，numpy 将自动触发广播机制, b通过广播与a兼容
#
# # 广播的规则:
# # 让所有输入数组都向其中形状最长的数组看齐，形状中不足的部分都通过在前面加 1 补齐。
# # 输出数组的形状是输入数组形状的各个维度上的最大值。
# # 如果输入数组的某个维度和输出数组的对应维度的长度相同或者其长度为 1 时，这个数组能够用来计算，否则出错。
# # 当输入数组的某个维度的长度为 1 时，沿着此维度运算时都用此维度上的第一组值。
# a = np.array([[ 0, 0, 0],
#            [10,10,10],
#            [20,20,20],
#            [30,30,30]])
# b = np.array([1,2,3])
# print(a + b)
#
# a = np.array([[ 0, 0, 0],
#            [10,10,10],
#            [20,20,20],
#            [30,30,30]])
# b = np.array([1,2,3])
# bb = np.tile(b, (4, 1))  # 重复 b 的各个维度
# print(a + bb)

# # numpy.nditer 提供了一种灵活访问一个或者多个数组元素的方式
# a = np.arange(6).reshape(2,3)
# print ('原始数组是：')
# print (a)
# print ('\n')
# print ('迭代输出元素：')
# for x in np.nditer(a):
#     print (x, end=", " )
# print ('\n')
#
# # a.T 为 a 的转置矩阵
# for x in np.nditer(a.T):
#     print(x, end=", ")
# print('\n')
#
# # c按行输出，f按列输出，A原顺序，K元素在内存中出现的顺序
# for x in np.nditer(a.T.copy(order='C')):
#     print(x, end=", ")
# print('\n')

# # 关于转置和c/f风格的展示
# a = np.arange(0,60,5)
# a = a.reshape(3,4)
# print ('原始数组是：')
# print (a)
# print ('\n')
# print ('原始数组的转置是：')
# b = a.T
# print (b)
# print ('\n')
# print ('以 C 风格顺序排序：')
# c = b.copy(order='C')
# print (c)
# for x in np.nditer(c):
#     print (x, end=", " )
# print  ('\n')
# print  ('以 F 风格顺序排序：')
# c = b.copy(order='F')
# print (c)
# for x in np.nditer(c):
#     print (x, end=", " )

# # nditer 对象有另一个可选参数 op_flags
# # 默认情况下，nditer 将视待迭代遍历的数组为只读对象（read-only），
# # 为了在遍历数组的同时，实现对数组元素值得修改，必须指定 read-write 或者 write-only 的模式
# a = np.arange(0,60,5)
# a = a.reshape(3,4)
# print ('原始数组是：')
# print (a)
# print ('\n')
# for x in np.nditer(a, op_flags=['readwrite']):
#     x[...]=2*x
# print ('修改后的数组是：')
# print (a)

# # 如果两个数组是可广播的，nditer 组合对象能够同时迭代它们
# # 假设数组 a 的维度为 3X4，数组 b 的维度为 1X4 ，则使用以下迭代器（数组 b 被广播到 a 的大小）
# a = np.arange(0,60,5)
# a = a.reshape(3,4)
# print  ('第一个数组为：')
# print (a)
# print  ('\n')
# print ('第二个数组为：')
# b = np.array([1,  2,  3,  4], dtype =  int)
# print (b)
# print ('\n')
# print ('修改后的数组为：')
# for x,y in np.nditer([a,b]):
#     print ("%d:%d"  %  (x,y), end=", " )

# numpy.ndarray.flat 是一个数组元素迭代器
# 每一列为一组数据，一共三组数据
a = np.arange(9).reshape(3, 3)
c = np.dot(a,a.T)/3
# 计算特征值
t = np.linalg.eigvals(c)
# 计算特征向量
s = np.linalg.eig(c)
s1 = s[1]
# 所有特征值中，第一个特征值大于1，其余均小于1，选择第一个特征值作为主成分进行分析
print(t)
# 进行函数投影，特征值对应的特征向量
print(s1[0])
# 降维后的结果
result = np.dot(s1[0],a)
print(np.dot(s1[0:2],a))
print(np.dot(s1[0:2],a)[0:2,0])
# 输出降维后的结果
print(result)