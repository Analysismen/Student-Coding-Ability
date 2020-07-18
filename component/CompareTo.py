import json
import component.averageScore as avg
import userComponent.difficultMain as diff

return_dict = {}
resultdict = {'字符串': [], '排序算法': [], '线性表': [], '数字操作': [], '查找算法': [], '树结构': [], '数组': [], '图结构': []}
avg_dict = {'字符串': 0, '排序算法': 0, '线性表': 0, '数字操作': 0, '查找算法': 0, '树结构': 0, '数组': 0, '图结构': 0}
theDict = {}


def jsonRead(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    data = json.load(f)
    for each in data:
        eachRecord = data[each]
        cases = eachRecord['cases']
        for eachCase in cases:
            case_type = eachCase['case_type']
            case_id = eachCase['case_id']
            avg_score = theDict[case_id]
            resultdict[case_type].append(avg_score)
    f.close()


def get_avg():
    temp = []
    temp = resultdict['字符串']
    avg_dict['字符串'] = diff.aver(temp)
    temp = resultdict['排序算法']
    avg_dict['排序算法'] = diff.aver(temp)
    temp = resultdict['线性表']
    avg_dict['线性表'] = diff.aver(temp)
    temp = resultdict['树结构']
    avg_dict['树结构'] = diff.aver(temp)
    temp = resultdict['数组']
    avg_dict['数组'] = diff.aver(temp)
    temp = resultdict['图结构']
    avg_dict['图结构'] = diff.aver(temp)
    temp = resultdict['数字操作']
    avg_dict['数字操作'] = diff.aver(temp)
    temp = resultdict['查找算法']
    avg_dict['查找算法'] = diff.aver(temp)


def jsonSecondRead(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    data = json.load(f)
    for each in data:
        eachRecord = data[each]
        cases = eachRecord['cases']
        for eachCase in cases:
            case_type = eachCase['case_type']
            case_id = eachCase['case_id']
            avg_score = theDict[case_id]
            final_com = avg_score - avg_dict[case_type]
            # 正分比较简单
            return_dict[case_id] = final_com
    f.close()


def main_thread(file_path):
    global theDict
    theDict = avg.main_thread(file_path)
    jsonRead(file_path)
    get_avg()
    jsonSecondRead(file_path)
    return return_dict


if __name__ == '__main__':
    main_thread()