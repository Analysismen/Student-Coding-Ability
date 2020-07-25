import Usercomponent.userScore as user_score
import Usercomponent.Fraction as frac
import Usercomponent.Time as time
import component.normalize as nom
import os
import json
import numpy as np

main_array = []
score_array = [30, 70, 77, 98, 70, 85, 89, 75, 37]
file_path = os.path.abspath(os.path.join(os.getcwd(), "../")).replace('\\', '/') + '/test_data.json'
file_path_style = os.path.abspath(os.path.join(os.getcwd(), "../")).replace('\\', '/') + '/CodingStyleOutPut.json'
for i in range(9):
    temp = []
    for j in range(5):
        temp.append(0)
    main_array.append(temp)

for i in range(9):
    main_array[i][0] = 1


def json_read():
    global main_array
    f = open(file_path_style, 'r', encoding='utf-8')
    data = json.load(f)
    data = nom.min_max_normalize(data)
    main_array[0][4] = data['3544']
    main_array[1][4] = data['48117']
    main_array[2][4] = data['58744']
    main_array[3][4] = data['60606']
    main_array[4][4] = data['60619']
    main_array[5][4] = data['60708']
    main_array[6][4] = data['60728']
    main_array[7][4] = data['60797']
    main_array[8][4] = data['61143']


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

    temp_return = time.main_thread(file_path)
    temp_return = nom.min_max_normalize(temp_return)
    main_array[0][3] = temp_return['3544']
    main_array[1][3] = temp_return['48117']
    main_array[2][3] = temp_return['58744']
    main_array[3][3] = temp_return['60606']
    main_array[4][3] = temp_return['60619']
    main_array[5][3] = temp_return['60708']
    main_array[6][3] = temp_return['60728']
    main_array[7][3] = temp_return['60797']
    main_array[8][3] = temp_return['61143']

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
    json_read()
    main_thread()
