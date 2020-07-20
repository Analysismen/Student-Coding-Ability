import json
import component.averageScore as avg

# user_id最小为2843,最大为61715，共有271个

# 存储学生参与的题目数量
nums = [0] * 61800
# 记录学生的总(初始)得分
scores = [0] * 61800


def jsonRead(file_path):
    average_score_dict = avg.main_thread(file_path)
    f = open(file_path, 'r', encoding='utf-8')
    data = json.load(f)
    for each in data:
        eachRecord = data[each]
        user_id = eachRecord['user_id']
        cases = eachRecord['cases']
        for eachCase in cases:
            uploads = eachCase['upload_records']
            case_id = eachCase['case_id']
            sub_aver = eachCase['final_score'] - average_score_dict[case_id]  # 本题得分-本题平均值
            nums[int(user_id)] += 1
            scores[int(user_id)] += float(sub_aver)
    f.close()


def main_thread(file_path):
    jsonRead(file_path)
    dictCTA = {}
    for i in range(2800, 61800):
        if (nums[i] != 0):
            # 存入字典，保留两位小数
            dictCTA[str(i)] = round(float(scores[i] / nums[i]), 2)
    return dictCTA
