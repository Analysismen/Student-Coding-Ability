import component.FirstGit as firstgit
import component.averageScore as avg
import component.CompareTo as com
import component.HalfSlope as slope
import component.FinalScore as final
import component.FractionalRatio as frac
import component.normalize as nomal
import component.timeToSolve as time
import numpy

diff_return = []
file_path = 'E:/coding/python/Question-Difficulty/sample.json'

for n in range(3000):
    temp = []
    for m in range(7):
        temp.append(0)
    diff_return.append(temp)


def aver(num_list):  # 对列表取平均值
    s = 0
    for x in num_list:
        s += x
    return s / len(num_list)


def main_thread():
    temp_return = firstgit.main_thread(file_path)
    temp_return = nomal.min_max_normalize(temp_return)
    temp_case_list = temp_return.keys()
    for case_id in temp_case_list:
        diff_return[int(case_id)][0] = temp_return[case_id]

    temp_return = final.main_thread(file_path)
    temp_return = nomal.min_max_normalize(temp_return)
    temp_case_list = temp_return.keys()
    for case_id in temp_case_list:
        diff_return[int(case_id)][1] = temp_return[case_id]

    temp_return = avg.main_thread(file_path)
    temp_return = nomal.min_max_normalize(temp_return)
    temp_case_list = temp_return.keys()
    for case_id in temp_case_list:
        diff_return[int(case_id)][2] = temp_return[case_id]

    temp_return = frac.main_thread(file_path)
    temp_return = nomal.min_max_normalize(temp_return)
    temp_case_list = temp_return.keys()
    for case_id in temp_case_list:
        diff_return[int(case_id)][3] = temp_return[case_id]

    temp_return = slope.main_thread(file_path)
    temp_return = nomal.min_max_normalize(temp_return)
    temp_case_list = temp_return.keys()
    for case_id in temp_case_list:
        diff_return[int(case_id)][4] = temp_return[case_id]

    temp_return = time.main_thread(file_path)
    temp_return = nomal.min_max_normalize(temp_return)
    temp_case_list = temp_return.keys()
    for case_id in temp_case_list:
        diff_return[int(case_id)][5] = temp_return[case_id]

    temp_return = com.main_thread(file_path)
    temp_return = nomal.min_max_normalize(temp_return)
    temp_case_list = temp_return.keys()
    for case_id in temp_case_list:
        diff_return[int(case_id)][6] = temp_return[case_id]

    for i in range(3000):
        num = aver(diff_return[i])
        for j in range(7):
            diff_return[i][j] -= num

    matrix_diff_origin = numpy.array(diff_return)
    # use numpy to calculate covariance(协方差) matrix of the matrix and view each row as a var
    cov_matrix = numpy.cov(matrix_diff_origin, rowvar=False)
    # calculate matrix eigenvalues of the matrix
    # eig_matrix_list[0]特征值，[1]特征向量
    eig_matrix_list = numpy.linalg.eig(cov_matrix)
    eig_matrix_value = list(numpy.linalg.eigvals(cov_matrix))
    main_var_index = eig_matrix_value.index(max(eig_matrix_value))  # eig_matrix_list[0].index(max(eig_matrix_value))
    # have Eigenvector of the matrix
    eig_vector_matrix = numpy.array(list(eig_matrix_list[1][main_var_index]))
    # transpose the matrix
    trans_eig_vec_matrix = eig_vector_matrix.transpose()  # numpy.transpose(eig_vector_matrix)
    # 两矩阵相乘
    res_matrix = list(numpy.dot(matrix_diff_origin, trans_eig_vec_matrix))
    for i in range(3000):
        res_matrix[i] = float(res_matrix[i])

    min_val = min(res_matrix)
    max_val = max(res_matrix)
    sub_val = max_val - min_val
    for i in range(len(res_matrix)):
        res_matrix[i] = round((res_matrix[i] - min_val)/sub_val,2)

    # print(res_matrix)

    return res_matrix


if __name__ == '__main__':
    main_thread()
