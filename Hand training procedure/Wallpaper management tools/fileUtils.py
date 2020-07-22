#coding=gbk
import Http
import os

file_path = r'D:\my picture2'
file_pathes = []

def save_file(url):
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    os.chdir(file_path)
    response = Http.visitUrl_response(url)
    content = response.content
    #截取url
    file_name = url.split(r'/')[-1]
    with open(file_name,'wb') as f:
        if not os.path.exists(r'/'+file_name):
            f.write(content)
            abs_path = file_path+'\\'+ file_name
            file_pathes.append(abs_path)
            print(abs_path,'has saved as a file')
            return abs_path
        else:
            print(file_name,'hax exist')

def removeAllPic():
    for i in os.listdir(file_path):
        if 'background.db' in i:
            continue
        else :
            abs_path = file_path + '\\' + i
            print('remove : ', abs_path)
            os.remove(abs_path)
