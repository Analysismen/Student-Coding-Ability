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
        return float(studentScore)
    except:
        return float('0.00')


def getLine(path):
    count = 0
    try:
        f = open(path, "r", encoding='utf-8')
        for line in f.readlines():
            count = count + 1
        return count
    except:
        return 1

def jsonRead(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    data = json.load(f)
    for each in data:
        codeScored = 0
        codeNumber = 0
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
            path = '../data/' + str(userId) + '/' + case_id + '/' + str(finalUploads) + '/main.py'
            score = getStudentScore(path)
            lineNumber = getLine(path)
            codeScored += (score + 20)/3 * lineNumber
            codeNumber += 1
        try:
            dictOfStudent[str(userId)] = round(codeScored / codeNumber, 2)
        except:
            dictOfStudent[str(userId)] = round(-5,2)
        print(dictOfStudent)
        # print(271-len(dictOfStudent))
    with open("../CodingStyleOutPut.json", "w") as Coding:
        json.dump(dictOfStudent, Coding)
    # print("加载入文件完成...")
    Coding.close()
    f.close()


def main_thread(file_path):
    jsonRead(file_path)
    return dictOfStudent


if __name__ == '__main__':
    main_thread('D:/Question-Difficulty/test_data.json')
