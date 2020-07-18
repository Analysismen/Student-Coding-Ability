import concurrent
import json
import urllib.request, urllib.parse
import os
import string
import zipfile
import concurrent.futures


def download(data):
    # 存储就用data.values()提供的嵌套字典
    dict = data.values()
    for user in data.values():
        userid = user['user_id']
        cases = user['cases']

        # tmp/user文件夹
        if not os.path.exists('.\\tmp\\' + str(userid)):
            os.mkdir('.\\tmp\\' + str(userid))
        for case in cases:
            caseid = case['case_id']

            # tmp/user/case
            if not os.path.exists('.\\tmp\\' + str(userid) + '\\' + str(caseid)):
                os.mkdir('.\\tmp\\' + str(userid) + '\\' + str(caseid))

            # url要把中文字符和空格quote
            fileurl = urllib.parse.quote(case['case_zip'], safe=string.printable).replace(" ", "%20")

            # 题目zip
            filename = os.path.basename(case['case_zip'])
            if not os.path.isfile('.\\tmp\\' + str(userid) + '\\' + str(caseid) + '\\' + filename):
                try:
                    urllib.request.urlretrieve(fileurl, '.\\tmp\\' + str(userid) + '\\' + str(caseid) + '\\' + filename)
                    print('下载' + '.\\tmp\\' + str(userid) + '\\' + str(caseid) + '\\' + filename)
                except  Exception as e:
                    print(str(e))
                    print('.\\tmp\\' + str(userid) + '\\' + str(caseid) + '\\' + filename + '下载失败')
            else:
                print('.\\tmp\\' + str(userid) + '\\' + str(caseid) + '\\' + filename + '已存在')

            # 提交记录
            for upload_record in case['upload_records']:
                uploadid = upload_record['upload_id']
                codezipname = str(uploadid) + '.zip'
                codeurl = upload_record['code_url']

                if not os.path.isfile('.\\tmp\\' + str(userid) + '\\' + str(caseid) + '\\' + codezipname):
                    try:
                        urllib.request.urlretrieve(codeurl,
                                                   '.\\tmp\\' + str(userid) + '\\' + str(caseid) + '\\' + codezipname)
                        print('下载' + '.\\tmp\\' + str(userid) + '\\' + str(caseid) + '\\' + codezipname)

                        # zip套zip解压
                        z = zipfile.ZipFile('.\\tmp\\' + str(userid) + '\\' + str(caseid) + '\\' + codezipname, 'r')
                        inzipname = z.namelist()[0]
                        z.extractall('.\\tmp\\' + str(userid) + '\\' + str(caseid) + '\\')
                        result_z = zipfile.ZipFile('.\\tmp\\' + str(userid) + '\\' + str(caseid) + '\\' + inzipname)

                        # 最终解压到data/userid/caseid/uploadid
                        print('解压到' + '.\\data\\' + str(userid) + '\\' + str(caseid) + '\\' + str(uploadid) + '\\')
                        result_z.extractall(
                            '.\\data\\' + str(userid) + '\\' + str(caseid) + '\\' + str(uploadid) + '\\')
                    except Exception as e:
                        print(str(e))
                        print('.\\tmp\\' + str(userid) + '\\' + str(caseid) + '\\' + codezipname + '下载失败')
                else:
                    print('.\\tmp\\' + str(userid) + '\\' + str(caseid) + '\\' + codezipname + '已存在')


if __name__ == '__main__':
    f = open('test_data.json', encoding='utf-8')
    res = f.read()
    data = json.loads(res)  # 加载json数据
    if not os.path.exists('.\\tmp'):
        os.mkdir('.\\tmp')
    with concurrent.futures.ProcessPoolExecutor(os.cpu_count()) as executor:
        executor.submit(download, data)
    print("Download Successfully!")
