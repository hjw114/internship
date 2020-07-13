#main.py
#coding=gbk
import getBgUrls
import fileUtils
import threading
import SetBg
import random
import db
import time

def setBgUrl():
    #˯�����ӣ��ȴ���һ���߳���ȡͼƬutl �����������г���������������
    time.sleep(5)
    print('setBgUrl has executed')
    pic_urls = getBgUrls.pic_urls
    if len(pic_urls) > 0:
        abs_path = fileUtils.save_file(random.choice(pic_urls))
        SetBg.set_wallpaper(abs_path)
    #ÿСʱ��һ��
    threading.Timer(60,setBgUrl).start()


if __name__ == '__main__':
    times =  db.getStartTimes()
    #��һ��ʹ�ñ����� ���ô洢�����ݿ������
    if times == 0 :
        t1 = threading.Thread(target=getBgUrls.get_pic_urls_to_db).start()
    elif times <= 10:
        #������ݿ������url����Ϊ0��֤����;����ϣ�û�в���ɹ�����Ҫ���¿�ʼ
        urls = db.getUrls()
        if len(urls) == 0:
            t1 = threading.Thread(target=getBgUrls.get_pic_urls_to_db).start()
        else:
            # �����ݿ��ȡurl
            getBgUrls.pic_urls = urls
    else :
        db.removeDb()
        fileUtils.removeAllPic()
        t1 = threading.Thread(target=getBgUrls.get_pic_urls_to_db).start()
    setBgUrl()



#SetBg.py    
#coding=gbk
import win32api, win32con, win32gui

def set_wallpaper(img_path):
    # ��ָ��ע���·��
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # ���Ĳ���:2����,0����,6��Ӧ,10���,0ƽ��
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    # ���Ĳ���:1��ʾƽ��,������еȶ���0
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # ˢ������
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, img_path, win32con.SPIF_SENDWININICHANGE)
   
   
    
#Http.py    
#coding=gbk
from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
#����url������soup ������Ʒ���Ƶ�ʣ�����������֤��
def visitUrl(url):
    wb_data = requests.get(url, headers=headers)
    #print('webEncoding is ',wb_data.encoding)
   # wb_data.encoding = 'gbk'
   # print('webEncoding has set gbk')
    soup = BeautifulSoup(wb_data.text, 'lxml')
    time.sleep(0.2)
    return soup

def visitUrl_response(url):
    return requests.get(url, headers=headers)


    
#GetBgUrls.py    
#coding=gbk
import Http
from win32api import GetSystemMetrics
import db
pic_urls = []  # �洢���е�ͼƬurl
#������վ����ȡͼƬurl
def get_pic_urls_to_db():
    global pic_urls
    base_url = r'http://desk.zol.com.cn'
    hot_url = r'http://desk.zol.com.cn/pc/hot_1.html' #���У�������������
    #ϵͳ�ֱ���
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    width_height = str(width)+'x'+str(height)

    soup = Http.visitUrl(hot_url)
    for i in soup.select(r'li.photo-list-padding > a'):
        url = base_url + i.get('href')
        soup = Http.visitUrl(url)
        for tag_a in soup.select(r'#showImg > li > a'):
            # �ҵ��ʺ��Լ����Էֱ��ʵ�ͼƬ����
            soup = Http.visitUrl(base_url + tag_a.get('href'))
            for i in soup.select('#tagfbl > a'):
                if width_height in i.get('href'):
                    image_html = base_url + i.get('href')
                    #print('image_html : ',image_html)
                    soup = Http.visitUrl(image_html)
                    tag_imgs = soup.select('body > img')
                    if len(tag_imgs) > 0:
                        pic_urls.append(tag_imgs[0].get('src'))
                        print('has get image url',tag_imgs[0].get('src'))

    db.insertInto(pic_urls)



#fileUnits.py
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
    #��ȡurl
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
 


           
#db.py
#coding=gbk
import sqlite3
import os
print('db has import')
#����ÿʹ��ʮ�Σ���������ȡ����
file_path = r'D:\deskPicc'
if not os.path.exists(file_path):
    os.mkdir(file_path)
conn_main = sqlite3.connect(r'D:\deskPicc\background.db')


cursor = conn_main.execute(r'SELECT count(*) FROM sqlite_master WHERE type="table" AND name="t_config"')


for i in cursor:
    if i[0] == 0:
        #��һ�����г��򣬴������ݿ�config��,urls��
        conn_main.execute(r'create table t_config(start_times int)')
        conn_main.execute(r"insert into t_config('start_times') values(0)") #��ʼ��Ϊ0
        conn_main.execute(r'create table t_urls(url varchar(200))')
        conn_main.commit()


conn_main.close()

