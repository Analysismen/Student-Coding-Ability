import json
# 平均分
times = [0] * 3000
scores = [0] * 3000


def json_read(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    data = json.load(f)
    for each in data:
        each_record = data[each]
        cases = each_record['cases']
        for each_case in cases:
            final_score = each_case['final_score']
            case_id = each_case['case_id']
            times[int(case_id)] += 1
            scores[int(case_id)] += final_score
    f.close()


def main_thread(file_path):
    json_read(file_path)
    dict_average_score = {}
    for i in range(3000):
        if times[i] != 0:
            dict_average_score[str(i)] = round(float(scores[i] / times[i]), 2)
    return dict_average_score
