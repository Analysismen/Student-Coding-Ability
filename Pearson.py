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
            if p < 0.05 and i != j:
                if corr > 0.8 and [j, i] not in positive_relations:
                    positive_relations.append([i, j])
                    # list_merge(positive_relations)
                if corr < -0.8 and [j, i] not in negative_relations:
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

'''
def list_merge(l):  
    b, c = l[len(l) - 1]  
    a = 0
    res = False

    for i in range(len(l) - 1):
        if b in l[i]:
            if l[i][0] == b:
                a = l[i][1]
            else:
                a = l[i][0]
            for j in range(len(l) - 1):
                if l[j] == [a, c] or l[j] == [c, a]:
                    res = True
                    l.remove([b, c])
                    l.remove(l[j])
                    l[i].append(c)
                    break
        if c in l[i]:
            if l[i][0] == c:
                a = l[i][1]
            else:
                a = l[i][0]
            for j in range(len(l) - 1):
                if l[j] == [a, b] or l[j] == [b, a]:
                    res = True
                    l.remove([b, c])
                    l.remove(l[j])
                    l[i].append(b)
                    break
        if res: break
    return l

'''