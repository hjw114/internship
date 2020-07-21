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
    #睡五秒钟，等待另一个线程爬取图片utl 这样可以运行程序，立即更换桌面
    time.sleep(5)
    print('setBgUrl has executed')
    pic_urls = getBgUrls.pic_urls
    if len(pic_urls) > 0:
        abs_path = fileUtils.save_file(random.choice(pic_urls))
        SetBg.set_wallpaper(abs_path)
    #每小时换一次
    threading.Timer(60,setBgUrl).start()


if __name__ == '__main__':
    times =  db.getStartTimes()
    #第一次使用本程序 调用存储到数据库的爬虫
    if times == 0 :
        t1 = threading.Thread(target=getBgUrls.get_pic_urls_to_db).start()
    elif times <= 10:
        #如果数据库的数据url长度为0，证明中途被打断，没有插入成功，需要重新开始
        urls = db.getUrls()
        if len(urls) == 0:
            t1 = threading.Thread(target=getBgUrls.get_pic_urls_to_db).start()
        else:
            # 从数据库获取url
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
    # 打开指定注册表路径
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 最后的参数:2拉伸,0居中,6适应,10填充,0平铺
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    # 最后的参数:1表示平铺,拉伸居中等都是0
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # 刷新桌面
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, img_path, win32con.SPIF_SENDWININICHANGE)
   
   
    
#Http.py    
#coding=gbk
from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
#访问url，返回soup 方便控制访问频率，避免输入验证码
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
pic_urls = []  # 存储所有的图片url
#解析网站，获取图片url
def get_pic_urls_to_db():
    global pic_urls
    base_url = r'http://desk.zol.com.cn'
    hot_url = r'http://desk.zol.com.cn/pc/hot_1.html' #所有，按下载量排序
    #系统分辨率
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    width_height = str(width)+'x'+str(height)

    soup = Http.visitUrl(hot_url)
    for i in soup.select(r'li.photo-list-padding > a'):
        url = base_url + i.get('href')
        soup = Http.visitUrl(url)
        for tag_a in soup.select(r'#showImg > li > a'):
            # 找到适合自己电脑分辨率的图片链接
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
 


           
#db.py
#coding=gbk
import sqlite3
import os
print('db has import')
#程序每使用十次，就重新爬取数据
file_path = r'D:\deskPicc'
if not os.path.exists(file_path):
    os.mkdir(file_path)
conn_main = sqlite3.connect(r'D:\deskPicc\background.db')


cursor = conn_main.execute(r'SELECT count(*) FROM sqlite_master WHERE type="table" AND name="t_config"')


for i in cursor:
    if i[0] == 0:
        #第一次运行程序，创建数据库config表,urls表
        conn_main.execute(r'create table t_config(start_times int)')
        conn_main.execute(r"insert into t_config('start_times') values(0)") #初始化为0
        conn_main.execute(r'create table t_urls(url varchar(200))')
        conn_main.commit()


conn_main.close()

