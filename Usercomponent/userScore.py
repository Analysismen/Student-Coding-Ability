import json
import Usercomponent.difficultMain as diff

res_dict = {}


def json_read():
    f = open('C:/Users/icimence/Desktop/Question Difficulty/test_data.json', 'r', encoding='utf-8')
    data = json.load(f)
    for each in data:
        each_record = data[each]
        cases = each_record['cases']
        user_id = int(each_record['user_id'])
        res_dict[user_id] = {}
        for each_case in cases:
            final_score = each_case['final_score']
            case_id = each_case['case_id']
            res_dict[user_id][case_id] = final_score * diff.main_thread()[case_id]  # 这里有问题，因为标准化导致了很多都是负数，并且不清楚负数的下限。
    f.close()


def main_thread():
    json_read()
    return res_dict
