import json

'''
调用load方法进行加载，返回时有两种方法，可以指定返回record还是info，如果是info数据格式如下：

dict={'user_id':'所有做过的题目的list'}

//做过的题目的列表中包括的信息依次是题目ID，题目类型，题目代码，最终得分，总共提交次数。

如果调用了record模式，返回数据如下：

dict={'user_id':[每一个题目[每一次提交]]}

每一次提交的列表依次包括了提交ID，提交时间戳，代码url，分数

然后是下载和解压方法

下载函数需要两个参数第一个参数是list类型的url，可以直接使用多个url进行下载，第二个是指定保存的目录，命名方式可以为'./filename/'前面的'./'不能缺少，会自动解压到同目录下，名字是文件名字+"_file"，经过处理可以进行循环解压，但是目前没有实现。

'''


def application(case_id, filepath):
    average_final_score = aver_final_score(case_id, filepath)
    average_slope = aver_slope(case_id, filepath)


def aver_final_score(case_id, filepath):
    final_score_list = []
    full_info_dic = load(filepath, "info").values()
    for user_all_cases in full_info_dic:
        for case in user_all_cases:
            if case_id == int(case[0]):
                final_score = case[3]
                final_score_list.append(final_score)
    # print(final_score_list)
    average_final_score = aver(final_score_list)
    print(average_final_score)
    return average_final_score


def aver_slope(case_id, filepath):
    slope_list = []
    full_record_dic = load(filepath, "record").values()
    for user_all_cases in full_record_dic:
        if str(case_id) not in user_all_cases:
            continue
        case = user_all_cases[str(case_id)]
        half_len = 0
        if len(case) // 2 * 2 == len(case):
            half_len = len(case) // 2
        else:
            half_len = len(case) // 2 + 1
        slope_list.append(max(case[0:half_len], key=lambda x: x[3])[3] / half_len)  # 改为一半提交的最大得分

    # print(slope_list)
    average_slope = aver(slope_list)
    print(average_slope)
    return average_slope


def aver(numlist):
    s = 0
    for x in numlist:
        s += x
    return s / len(numlist)


def load(filepath, method):
    data_json = open(filepath, encoding='UTF-8', errors='ignore')
    data = json.load(data_json, encoding='UTF-8')
    full_info_dic = {}
    full_record_dic = {}
    user = list(data.keys())
    for i in range(len(data)):
        user_info = data[user[i]]
        user_temp_list = []
        user_record_dic = {}
        user_id = user_info['user_id']
        cases = user_info['cases']
        for case in cases:
            records = case['upload_records']
            records_temp_list = []
            case_temp_list = [case['case_id'], case['case_type'], case['case_zip'], case['final_score'], len(records)]
            for record in records:
                record_temp_list = [record['upload_id'], record['upload_time'], record['code_url'], record['score']]
                records_temp_list.append(record_temp_list)
            user_record_dic[case['case_id']] = records_temp_list
            user_temp_list.append(case_temp_list)
        full_info_dic[user_id] = user_temp_list
        full_record_dic[user_id] = user_record_dic
    if method == "info":
        return full_info_dic
    else:
        return full_record_dic


if __name__ == "__main__":
    # print(load("sample.json", "info"))
    application(2908, "../sample.json")
