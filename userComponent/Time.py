import json

# user_id最小为2843,最大为61715，共有271个

# 存储学生参与的题目数量
nums = [0] * 61800
# 记录学生的总(初始)得分
scores = [0] * 61800


def jsonRead():
    f = open('../test_data.json', 'r', encoding='utf-8')
    data = json.load(f)
    for each in data:
        eachRecord = data[each]
        user_id = eachRecord['user_id']
        cases = eachRecord['cases']
        for eachCase in cases:
            uploads = eachCase['upload_records']
            if not uploads:
                continue
            else:
                time = float(uploads[-1]['upload_time'] - uploads[0]['upload_time'] / 1000)
            nums[int(user_id)] += 1
            scores[int(user_id)] += float(time)
    f.close()


jsonRead()
dictTime = {}
for i in range(2800, 61800):
    if (nums[i] != 0):
        # 存入字典，保留两位小数
        dictTime[str(i)] = round(float(scores[i] / nums[i]), 2)
print(dictTime)


def getDictTime():
    return dictTime
