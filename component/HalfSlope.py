import json

# 存储题目被提交次数
times = [0] * 3000
# 记录参与人总体分数变动值
scores = [0] * 3000


def jsonRead():
    f = open('../test_data.json', 'r', encoding='utf-8')
    data = json.load(f)
    for each in data:
        eachRecord = data[each]
        cases = eachRecord['cases']
        for eachCase in cases:
            uploads = eachCase['upload_records']
            case_id = eachCase['case_id']
            half_len = len(uploads) // 2 + 1 if len(uploads) % 2 else len(uploads) // 2
            # 改为一半提交的最大得分
            half_slope = max(uploads[0:half_len], key=lambda x: x['score'])['score'] / half_len if len(uploads) != 0 else 0
            times[int(case_id)] += 1
            scores[int(case_id)] += float(half_slope)
    f.close()


def min_max_normalize(dict_before):
    max_value = max(zip(dict_before.values(), dict_before.keys()))[0]
    min_value = min(zip(dict_before.values(), dict_before.keys()))[0]
    max_sub = max_value - min_value
    dict_after = {}
    for key, val in dict_before.items():
        val = round(100 * (val - min_value) / max_sub, 2)
        dict_after[key] = val
    return dict_after


jsonRead()
dictHalfSlope = {}
for i in range(0, 3000):
    if (times[i] != 0):
        dictHalfSlope[str(i)] = float(scores[i] / times[i])

dictHalfSlope = min_max_normalize(dictHalfSlope)
print(dictHalfSlope)


def getDictHalfSlope():
    return dictHalfSlope
