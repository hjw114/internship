import requests
import os
import sys
import urllib.request as urllib
from lxml import etree
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


# 网页抓取
class Crawler_message(object):

     def __init__(self,start_url):
          self.start_url = start_url

     def run(self):
          # 请求
          User_Agent = UserAgent().random  # 伪装爬虫的登录浏览器
          headers = {'User-Agent': User_Agent}
          request = urllib.Request(url = start_url, headers = headers)
          # 爬取结果
          response = urllib.urlopen(request)
          data = response.read()
          # 设置解码方式
          data = data.decode('utf-8')
          # 打印结果
          print(data)
          # 打印爬取网页的各类信息
          print(type(response))
          print(response.geturl())
          print(response.info())
          print(response.getcode())


# 图片爬虫
class Crawler_pic(object):
     index = 1

     def __init__(self,start_url):
          self.start_url = start_url


     @staticmethod
     def request(url, **kwargs):
          try:
               page = requests.get(url,**kwargs)
               return page.text
          except:
               return ''
     # 求取网页源码


     @property
     def get_max_page(self):
          html = self.request(self.start_url)
          html = etree.HTML(html)
          pages = html.xpath('//li[@class = "l_reply_num"]//@max-page')
          max_page,*_ = pages
          return int(max_page)
     # 求取最大页码


     def get_all_urls(self,max_page):
          for i in range(1,max_page + 1):
               yield (self.start_url + '?pn={}'.format(i))
     # 求取本贴所有图片地址


     @classmethod
     def get_imgs(cls,html):
          soup = BeautifulSoup(html, 'html.parser')
          img_urls = soup.find_all('img', class_='BDE_Image')
          for img in img_urls:
               print ("正在下载第{}张图片".format(cls.index))
               urllib.urlretrieve(img.get("src"),r'E:\pic\{}.jpg'.format(cls.index))
               cls.index += 1
     # 爬取图片


     def run(self):
          max_page = self.get_max_page
          urls = self.get_all_urls(max_page)
          for url in urls:
               User_Agent = UserAgent().random     # 伪装爬虫的登录浏览器
               headers = {'User-Agent':User_Agent}
               html = self.request(url,headers = headers)
               self.get_imgs(html)


# 小说爬虫
class Crawler_novel(object):

     def __init__(self,start_url):
          self.start_url = start_url
          self.server = 'http://www.biqukan.com/'
          self.target = start_url
          self.names = []  # 存放章节名
          self.urls = []  # 存放章节链接
          self.nums = 0  # 章节数

     """
     函数说明:获取下载链接
     Parameters:
         无
     Returns:
         无
     Modify:
         2017-09-13
     """

     def get_download_url(self):
          req = requests.get(url = self.target)
          req.encoding = 'GB2312'
          html = req.text
          div_bf = BeautifulSoup(html, features = "lxml")
          div = div_bf.find_all('div', class_='listmain')
          a_bf = BeautifulSoup(str(div[0]),  features = "lxml")
          a = a_bf.find_all('a')
          self.nums = len(a[15:])  # 剔除不必要的章节，并统计章节数
          for each in a[15:]:
               self.names.append(each.string)
               self.urls.append(self.server + each.get('href'))

     """
     函数说明:获取章节内容
     Parameters:
         target - 下载连接(string)
     Returns:
         texts - 章节内容(string)
     Modify:
         2017-09-13
     """

     def get_contents(self, target):
          req = requests.get(url = target)
          req.encoding = 'GB2312'
          html = req.text
          bf = BeautifulSoup(html, features = "lxml")
          texts = bf.find_all('div', class_ = 'showtxt')
          texts = texts[0].text.replace('\xa0' * 8, '\n\n')
          return texts

     """
     函数说明:将爬取的文章内容写入文件
     Parameters:
         name - 章节名称(string)
         path - 当前路径下,小说保存名称(string)
         text - 章节内容(string)
     Returns:
         无
     Modify:
         2017-09-13
     """

     def writer(self, name, path, text):
          write_flag = True
          with open(path, 'a', encoding = 'UTF-8') as f:
               f.write(name + '\n')
               f.writelines(text)
               f.write('\n\n')

     def run(self):
          self.get_download_url()
          print('小说开始下载：')
          for i in range(self.nums):
               self.writer(self.names[i], '沧元图.txt', self.get_contents(self.urls[i]))
               sys.stdout.write("  已下载:%.3f%%" % float(i / self.nums) + '\r')
               sys.stdout.flush()
          print('小说下载完成')




# 主程序
if __name__=='__main__':
     while True:
          choice = input("(0) 网页抓取  (1) 爬取贴吧图片  (2) 爬取小说  (3)退出  Please input your choice(0/1/2): ")

          if choice in '':
               print("崩溃了，求求你输入点东西")
               continue

          url = input("请输入需要处理的网站网址：(目前不提供手动输入，采用默认)")

          if choice in '0':
               start_url = "http://www.baidu.com/"
               crawler = Crawler_message(start_url)
               crawler.run()
               continue

          elif choice in '1':
               start_url = "https://tieba.baidu.com/p/3910085328"  # 被爬取的帖子网址
               if not os.path.exists('E:\pic'):  # 看是否有该文件夹，没有则创建文件夹
                    os.mkdir('E:\pic')
               crawler = Crawler_pic(start_url)
               crawler.run()
               continue

          elif choice in '2':
               start_url = "https://www.biqukan.com/38_38836/"
               dl = Crawler_novel(start_url)
               dl.run()
               continue

          elif choice in '3':
               break;
          
          else:
               print("Invalid input, Try again.")
               continue


