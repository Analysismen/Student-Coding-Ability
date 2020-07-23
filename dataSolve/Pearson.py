import json
from scipy.stats import pearsonr
import Usercomponent.FirstUpload as firstUpload
import Usercomponent.Fraction as fraction
import Usercomponent.Time as time
import Usercomponent.userScore as userScore
import Usercomponent.CompareToAverage as compare
import component.normalize as normal
import os
import numpy as np

diff_return = []
file_path = os.path.abspath(os.path.join(os.getcwd(), "../")).replace('\\', '/') + '/test_data.json'


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

    positive_relations = []
    negative_relations = []

    corr_matrix_list = []
    p_matrix_list = []
    for i in range(len(a)):
        tmp_0 = []
        tmp_1 = []
        for j in range(len(a)):
            corr, p = pearsonr(a[i], a[j])
            tmp_0.append(corr)
            tmp_1.append(p)
            if p < 0.01 and i != j:
                if corr > 0.9 and [j, i] not in positive_relations:
                    positive_relations.append([i, j])
                    # list_merge(positive_relations)
                if corr < -0.9 and [j, i] not in negative_relations:
                    negative_relations.append([i, j])
                    # list_merge(negative_relations)
        corr_matrix_list.append(tmp_0)
        p_matrix_list.append(tmp_1)

    corr_matrix = np.asarray(corr_matrix_list)
    p_matrix = np.asarray(p_matrix_list)
    print(corr_matrix.round(2))
    print(p_matrix.round(2))

    positive_negative = [positive_relations, negative_relations]
    print(positive_negative)
    return positive_negative


if __name__ == '__main__':
    main_thread()
