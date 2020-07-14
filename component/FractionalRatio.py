import json

# 存储题目被提交次数
times = [0] * 3000
# 记录参与人总体分数变动值
scores = [0] * 3000


def jsonRead(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    data = json.load(f)
    for each in data:
        eachRecord = data[each]
        cases = eachRecord['cases']
        for eachCase in cases:
            uploads = eachCase['upload_records']
            case_id = eachCase['case_id']
            final_score = eachCase['final_score']
            if not uploads:
                final_score = 0
            else:
                firstGit = uploads[0]['score']
            times[int(case_id)] += len(uploads)
            scores[int(case_id)] += float(final_score)
    f.close()


def main_thread(file_path):
    jsonRead(file_path)
    dictFractionalRatio = {}
    for i in range(0, 3000):
        if times[i] != 0:
            # 存入字典，保留两位小数
            dictFractionalRatio[str(i)] = round(float(scores[i] / times[i]), 2)
    return dictFractionalRatio