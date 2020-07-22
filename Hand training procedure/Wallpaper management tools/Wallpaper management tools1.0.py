#main.py
#coding=gbk
#该项目为main项目，运行这个即可 功能：一分钟替换一次墙纸，图片由爬虫在网上获取
import threading
import random
import time
import db
import getBgUrls
import fileUtils
import SetBg

def setBgUrl():
    #睡五秒钟，等待另一个线程爬取图片utl 这样可以运行程序，立即更换桌面
    time.sleep(5)
    print('setBgUrl has executed')
    pic_urls = getBgUrls.pic_urls
    if len(pic_urls) > 0:
        abs_path = fileUtils.save_file(random.choice(pic_urls))
        SetBg.set_wallpaper(abs_path)
    #一分钟更换一次
    threading.Timer(60,setBgUrl).start()
if __name__ == '__main__':
    times = db.getStartTimes()
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
