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

