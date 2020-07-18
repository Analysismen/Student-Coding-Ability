import json
import subprocess

dictOfStudent = {}


def getStudentScore(path):
    try:
        process = subprocess.Popen("pylint --rcfile=pylint.conf " + path, shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        command_output = process.stdout.read().decode('gb18030')
        splitOutCome = command_output.split('\n')
        totalScore = splitOutCome[-3][28:-2]
        studentScore = totalScore[0:-3]
        if studentScore == '':
            studentScore = '0.00'
        return studentScore
    except:
        return '0.00'


def jsonRead(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    data = json.load(f)
    for each in data:
        eachRecord = data[each]
        cases = eachRecord['cases']
        userId = eachRecord['user_id']
        for eachCase in cases:
            uploads = eachCase['upload_records']
            case_id = eachCase['case_id']
            if len(uploads) == 0:
                break
            else:
                finalUploads = uploads[-1]['upload_id']
            score = getStudentScore('../data/' + str(userId) + '/' + case_id + '/' + str(finalUploads) + '/main.py')
            dictOfStudent[str(userId)+" "+str(case_id)] = round(float(score), 2)
    with open("../CodingStyleOutPut.json", "w") as Coding:
        json.dump(dictOfStudent, Coding)
    # print("加载入文件完成...")
    Coding.close()
    f.close()

def main_thread(file_path):
    jsonRead(file_path)
    return dictOfStudent

jsonRead('../sample.json')