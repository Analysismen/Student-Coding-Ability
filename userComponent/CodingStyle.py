import json
import subprocess

dictOfStudent = {}

def getStudentScore(path):
    process = subprocess.Popen("pylint --rcfile=pylint.conf " + path, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    command_output = process.stdout.read().decode('gb18030')
    splitOutCome = command_output.split('\n')
    totalScore = splitOutCome[-3][28:-2]
    studentScore = totalScore[0:-3]
    if studentScore == '':
        studentScore = '0.00'
    return studentScore

def jsonRead():
    f = open('../sample.json', 'r', encoding='utf-8')
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
            finalUploads = 0
            if len(uploads)==0:
                break
            else:
                finalUploads = uploads[-1]['upload_id']
            score = getStudentScore('../data/'+str(userId)+'/'+case_id+'/'+str(finalUploads)+'/main.py')
            codeScored += (float(score)+20)/3
            codeNumber += 1
        dictOfStudent[str(userId)] = round(codeScored/codeNumber,2)
    f.close()

jsonRead()
print(dictOfStudent)

def getDictOfStudent():
    return dictOfStudent