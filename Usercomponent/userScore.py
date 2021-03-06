import json
import Usercomponent.difficultMain as diff

res_dict = {}

def json_read(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    return_list = diff.main_thread()
    data = json.load(f)
    for each in data:
        each_record = data[each]
        cases = each_record['cases']
        user_id = int(each_record['user_id'])
        time = 0
        sum_score = 0
        for each_case in cases:
            final_score = each_case['final_score']
            case_id = each_case['case_id']
            sum_score += final_score * return_list[int(case_id)]
            time += 1
            res_dict[str(user_id)] = sum_score / time  # 这里有问题，因为标准化导致了很多都是负数，并且不清楚负数的下限。
    f.close()


def main_thread(file_path):
    json_read(file_path)
    return res_dict

