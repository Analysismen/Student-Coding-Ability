import json
# 最终分
# 存储题目被调用的次数/有多少人参与此题
times = [0] * 3000
# 记录参与人总分
scores = [0] * 3000


def jsonRead(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    data = json.load(f)
    for each in data:
        eachRecord = data[each]
        cases = eachRecord['cases']
        for eachCase in cases:
            case_id = eachCase['case_id']
            uploads = eachCase['upload_records']
            final_score = eachCase['final_score'] if len(uploads) != 0 else 0

            times[int(case_id)] += 1
            scores[int(case_id)] += float(final_score)
    f.close()


def main_thread(file_path):
    jsonRead(file_path)
    dictFinalScore = {}
    for i in range(0, 3000):
        if (times[i] != 0):
            dictFinalScore[str(i)] = float(scores[i] / times[i])
    return dictFinalScore
