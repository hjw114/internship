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
