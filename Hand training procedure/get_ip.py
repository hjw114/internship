import requests
from lxml import etree


def getinfo(ip):
    url = 'https://ipchaxun.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    r = requests.get(url + ip, headers=headers)
    html = etree.HTML(r.text)
    ls = html.xpath('//span[@class="name"]/text() | //span[@class="value"]/text()')
    return ls


if __name__ == '__main__':
    ip = input('请输入要查询的ip地址: ')
    ls = getinfo(str(ip))
    print(ls)
