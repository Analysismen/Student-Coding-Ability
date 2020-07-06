import json

# 存储题目被调用的次数/有多少人参与此题
times = [0] * 3000
# 记录参与人总分
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
            if (uploads == []):
                firstGit = 0
            else:
                firstGit = uploads[0]['score']
            times[int(case_id)] += 1
            scores[int(case_id)] += float(firstGit)
    f.close()


jsonRead()
dictFirstGit = {}
for i in range(0, 3000):
    if (times[i] != 0):
        # 存入字典，保留两位小数
        dictFirstGit[str(i)] = round(float(scores[i] / times[i]), 2)
print(dictFirstGit)


def getDictFirstGit():
    return dictFirstGit
