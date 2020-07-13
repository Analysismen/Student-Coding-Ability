import json

# 存储题目被调用的次数/有多少人参与此题
times = [0] * 3000
# 记录参与人总分
scores = [0] * 3000


def jsonRead():
    f = open('C:/Users/icimence/Desktop/Question Difficulty/test_data.json', 'r', encoding='utf-8')
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
dictFinalScore = {}
for i in range(0, 3000):
    if (times[i] != 0):
        dictFinalScore[str(i)] = float(scores[i] / times[i])

dictFinalScore = min_max_normalize(dictFinalScore)
print(dictFinalScore)


def getDictFinalScore():
    return dictFinalScore
