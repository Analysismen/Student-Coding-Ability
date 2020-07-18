import json
from scipy.stats import pearsonr
import userComponent.FirstUpload as firstUpload
import userComponent.Fraction as fraction
import userComponent.Time as time
import userComponent.UserScore as userScore
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

    f = open('SampleCodingStyleOutput.json', 'r', encoding='utf-8')  # codingStyle这个速度，还是直接读文件比较好
    data = json.load(f)
    temp_return = normal.min_max_normalize(data)
    temp_value_list = list(temp_return.values())
    diff_return.append(temp_value_list)

    a = np.asarray(diff_return)

    # print(a)
    # correlation_matrix = np.corrcoef(a, rowvar=True)
    # print(correlation_matrix.round(2))

    corr_matrix_list = []
    p_matrix_list = []
    for i in range(len(a)):
        tmp_0 = []
        tmp_1 = []
        for j in range(len(a)):
            corr, p = pearsonr(a[i], a[j])
            tmp_0.append(corr)
            tmp_1.append(p)
        corr_matrix_list.append(tmp_0)
        p_matrix_list.append(tmp_1)

    corr_matrix = np.asarray(corr_matrix_list)
    p_matrix = np.asarray(p_matrix_list)
    print(corr_matrix.round(2))
    print(p_matrix.round(2))
    list_return = [corr_matrix, p_matrix]
    print(list_return)
    return list_return


if __name__ == '__main__':
    main_thread()
