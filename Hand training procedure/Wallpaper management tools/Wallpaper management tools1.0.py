#main.py
#coding=gbk
#����ĿΪmain��Ŀ������������� ���ܣ�һ�����滻һ��ǽֽ��ͼƬ�����������ϻ�ȡ
import threading
import random
import time
import db
import getBgUrls
import fileUtils
import SetBg

def setBgUrl():
    #˯�����ӣ��ȴ���һ���߳���ȡͼƬutl �����������г���������������
    time.sleep(5)
    print('setBgUrl has executed')
    pic_urls = getBgUrls.pic_urls
    if len(pic_urls) > 0:
        abs_path = fileUtils.save_file(random.choice(pic_urls))
        SetBg.set_wallpaper(abs_path)
    #һ���Ӹ���һ��
    threading.Timer(60,setBgUrl).start()
if __name__ == '__main__':
    times = db.getStartTimes()
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
