import numpy as np  # 导入库
import json

f = open('sample.json', 'r', encoding='utf-8')
fStr = []
data = json.load(f)
for each in data:
    fStr.append(int(each))
print(fStr)
a = np.asarray(fStr)
print(a)
a.shape = (2, 5)
print(a)
correlation_matrix = np.corrcoef(a, rowvar=True)  # 相关性分析,rowvar=0表示对行作相关性分析
print(correlation_matrix.round(2))  # 打印输出相关性结果


