import Usercomponent.userScore as user_score
import Usercomponent.Fraction as frac
import component.normalize as nom
import numpy as np
import os

main_array = []
score_array = [30, 70, 77, 98, 70, 90, 89, 75, 37]
file_path = file_path = os.path.abspath(os.path.join(os.getcwd(), "../")).replace('\\', '/') + '/test_data.json'
for i in range(9):
    temp = []
    for j in range(3):
        temp.append(0)
    main_array.append(temp)

for i in range(9):
    main_array[i][0] = 1


def get_data():
    global main_array
    main_thread()
    main_array[0][0] = score_array[0]
    main_array[1][0] = score_array[1]
    main_array[2][0] = score_array[2]
    main_array[3][0] = score_array[3]
    main_array[4][0] = score_array[4]
    main_array[5][0] = score_array[5]
    main_array[6][0] = score_array[6]
    main_array[7][0] = score_array[7]
    main_array[8][0] = score_array[8]
    return main_array


def main_thread():
    global main_array
    global score_array
    temp_return = user_score.main_thread(file_path)
    temp_return = nom.min_max_normalize(temp_return)
    main_array[0][1] = temp_return['3544']
    main_array[1][1] = temp_return['48117']
    main_array[2][1] = temp_return['58744']
    main_array[3][1] = temp_return['60606']
    main_array[4][1] = temp_return['60619']
    main_array[5][1] = temp_return['60708']
    main_array[6][1] = temp_return['60728']
    main_array[7][1] = temp_return['60797']
    main_array[8][1] = temp_return['61143']

    temp_return = frac.main_thread(file_path)
    temp_return = nom.min_max_normalize(temp_return)
    main_array[0][2] = temp_return['3544']
    main_array[1][2] = temp_return['48117']
    main_array[2][2] = temp_return['58744']
    main_array[3][2] = temp_return['60606']
    main_array[4][2] = temp_return['60619']
    main_array[5][2] = temp_return['60708']
    main_array[6][2] = temp_return['60728']
    main_array[7][2] = temp_return['60797']
    main_array[8][2] = temp_return['61143']

    X_matrix = np.array(main_array)
    Y_matrix_t = np.array(score_array)
    Y_matrix = Y_matrix_t.transpose()
    res_vector_t = np.dot(np.dot(np.linalg.inv(np.dot(X_matrix.transpose(), X_matrix)), X_matrix.transpose()), Y_matrix)
    res_vector = list(res_vector_t.transpose())
    for i in range(len(res_vector)):
        res_vector[i] = float(res_vector[i])
    print(res_vector)
    return res_vector


if __name__ == '__main__':
    main_thread()
