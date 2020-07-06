import json

times = [0] * 3000
scores = [0] * 3000


def json_read():
    f = open('../test_data.json', 'r', encoding='utf-8')
    data = json.load(f)
    for each in data:
        each_record = data[each]
        cases = each_record['cases']
        for each_case in cases:
            uploads = each_case['upload_records']
            case_id = each_case['case_id']
            if not uploads:
                continue
            else:
                time = float(uploads[-1]['upload_time'] - uploads[0]['upload_time'] / 1000)
            times[int(case_id)] += 1
            scores[int(case_id)] += time
    f.close()


def main_thread():
    dict_total_time = {}
    for i in range(3000):
        if times[i] != 0:
            dict_total_time[str(i)] = round(float(scores[i] / times[i]), 2)
    return dict_total_time
