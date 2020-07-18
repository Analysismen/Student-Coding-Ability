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
    temp_return = firstUpload.main_thread(file_path)
    temp_return = normal.min_max_normalize(temp_return)
    temp_value_list = list(temp_return.values())
    diff_return.append(temp_value_list)

    temp_return = fraction.main_thread(file_path)
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

    temp_return = codingStyle.main_thread(file_path)           # 有点慢，估计test_data会很慢
    temp_return = normal.min_max_normalize(temp_return)
    temp_value_list = list(temp_return.values())
    diff_return.append(temp_value_list)

    # temp_return = userScore.main_thread(file_path)
    # temp_return = normal.min_max_normalize(temp_return)
    # temp_value_list = list(temp_return.values())
    # diff_return.append(temp_value_list)

    print(diff_return)

    a = np.asarray(diff_return)

    correlation_matrix = np.corrcoef(a, rowvar=True)
    print(correlation_matrix.round(2))                  # codingstyle 有除0的问题！！！！！
'''
 

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
    print(res_matrix)
    for i in range(2600, 2620):
        print(res_matrix[i])
    return res_matrix
'''



if __name__ == '__main__':
    main_thread()
