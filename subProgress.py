import subprocess

#调用命令行函数
def getStudentScore(path):
    process = subprocess.Popen("pylint --rcfile=pylint.conf " + path, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    process.wait()
    command_output = process.stdout.read().decode('gb18030')
    splitOutCome = command_output.split('\n')
    totalScore = splitOutCome[-3][28:-2]
    studentScore = totalScore[0:-3]
    fullScore = 10
    return studentScore

#传入文件路径
str = getStudentScore('npStudy.py')
print(str)