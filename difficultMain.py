import component.FirstGit as firstgit
import component.averageScore as avg
import component.CompareTo as com
import component.difficult as diff
import component.FractionalRatio as frac
import component.normalize as nomal
import component.timeToSolve as time
import numpy

diff_return = [[0, 0, 0, 0, 0, 0, 0]] * 3000

temp_return = firstgit.getDictFirstGit()
temp_return = nomal.min_max_normalize(temp_return)
temp_case_list = temp_return.keys()
for case_id in temp_case_list:
    diff_return[int(case_id)][0] = temp_return[case_id]

temp_return = firstgit.getDictFirstGit()
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

temp_return = firstgit.getDictFirstGit()
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


