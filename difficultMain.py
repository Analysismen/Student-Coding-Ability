import component.FirstGit as firstgit
import component.averageScore as avg
import component.CompareTo as com
import component.HalfSlope as slope
import component.FinalScore as final
import component.FractionalRatio as frac
import component.normalize as nomal
import component.timeToSolve as time
import component.final_ScoreAndSlope as avg_cal
import numpy

diff_return = [[0, 0, 0, 0, 0, 0, 0]] * 3000


def main_thread():
    temp_return = firstgit.getDictFirstGit()
    temp_return = nomal.min_max_normalize(temp_return)
    temp_case_list = temp_return.keys()
    for case_id in temp_case_list:
        diff_return[int(case_id)][0] = temp_return[case_id]

    temp_return = final.getDictFinalScore()
    temp_return = nomal.min_max_normalize(temp_return)
    temp_case_list = temp_return.keys()
    for case_id in temp_case_list:
        diff_return[int(case_id)][1] = temp_return[case_id]

    temp_return = avg.main_thread()
    temp_return = nomal.min_max_normalize(temp_return)
    temp_case_list = temp_return.keys()
    for case_id in temp_case_list:
        diff_return[int(case_id)][2] = temp_return[case_id]

    temp_return = frac.getDictFractionalRatio()
    temp_return = nomal.min_max_normalize(temp_return)
    temp_case_list = temp_return.keys()
    for case_id in temp_case_list:
        diff_return[int(case_id)][3] = temp_return[case_id]

    temp_return = slope.getDictHalfSlope()
    temp_return = nomal.min_max_normalize(temp_return)
    temp_case_list = temp_return.keys()
    for case_id in temp_case_list:
        diff_return[int(case_id)][4] = temp_return[case_id]

    temp_return = time.main_thread()
    temp_return = nomal.min_max_normalize(temp_return)
    temp_case_list = temp_return.keys()
    for case_id in temp_case_list:
        diff_return[int(case_id)][5] = temp_return[case_id]

    temp_return = com.main_thread()
    temp_return = nomal.min_max_normalize(temp_return)
    temp_case_list = temp_return.keys()
    for case_id in temp_case_list:
        diff_return[int(case_id)][6] = temp_return[case_id]

    for i in range(3000):
        num = avg_cal.aver(diff_return[i])
        for j in range(7):
            diff_return[i][j] -= num

    matrix_diff_origin = numpy.array(diff_return)
    # use numpy to calculate covariance(协方差) matrix of the matrix and view each row as a var
    cov_matrix = numpy.cov(matrix_diff_origin, rowvar=False)
    # calculate matrix eigenvalues of the matrix
    # eig_matrix_list[0]特征值，[1]特征向量
    eig_matrix_list = numpy.linalg.eig(cov_matrix)
    main_var_index = eig_matrix_list.index(min(cov_matrix[0]))
    # have Eigenvector of the matrix
    eig_vector_matrix = eig_matrix_list[1][main_var_index]
    # transpose the matrix
    trans_eig_vec_matrix = numpy.transpose(eig_vector_matrix)
    # 两矩阵相乘
    res_matrix = numpy.dot(trans_eig_vec_matrix, matrix_diff_origin)


if __name__ == '__main__':
    main_thread()
