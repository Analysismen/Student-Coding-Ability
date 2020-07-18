import json

import userComponent.FirstUpload as firstUpload
import userComponent.Fraction as fraction
import userComponent.Time as time
import userComponent.UserScore as userScore
import userComponent.CodingStyle as codingStyle
import userComponent.CompareToAverage as compare
import component.normalize as normal
import numpy as np


diff_return = []
file_path = 'E:/coding/python/Question-Difficulty/sample.json'

def main_thread():
    temp_return = userScore.main_thread(file_path)
    temp_return = normal.min_max_normalize(temp_return)
    temp_value_list = list(temp_return.values())
    diff_return.append(temp_value_list)

    temp_return = fraction.main_thread(file_path)
    temp_return = normal.min_max_normalize(temp_return)
    temp_value_list = list(temp_return.values())
    diff_return.append(temp_value_list)

    temp_return = firstUpload.main_thread(file_path)
    temp_return = normal.min_max_normalize(temp_return)
    temp_value_list = list(temp_return.values())
    diff_return.append(temp_value_list)

    temp_return = time.main_thread(file_path)
    temp_return = normal.min_max_normalize(temp_return)
    temp_value_list = list(temp_return.values())
    diff_return.append(temp_value_list)

    temp_return = compare.main_thread(file_path)
    temp_return = normal.min_max_normalize(temp_return)
    temp_value_list = list(temp_return.values())
    diff_return.append(temp_value_list)

    f = open('CodingStyleOutPut.json', 'r', encoding='utf-8')             # codingStyle这个速度，还是直接读文件比较好
    data = json.load(f)
    print(data)
    temp_return = normal.min_max_normalize(data)
    temp_value_list = list(temp_return.values())
    diff_return.append(temp_value_list)


    print(diff_return)

    a = np.asarray(diff_return)

    correlation_matrix = np.corrcoef(a, rowvar=True)
    print(correlation_matrix.round(2))                   # codingstyle 有除0的问题！！！！！
    return correlation_matrix

if __name__ == '__main__':
    main_thread()
