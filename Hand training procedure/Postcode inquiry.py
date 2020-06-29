from requests_html import HTMLSession
session=HTMLSession()#建立会话
postcode=input("请输入邮编:")
url="https://www.ip138.com/post/search.asp?zip="+postcode+"&action=zip2area"#网址储存
r=session.get(url)#取回内容
sel="body > div > div.container > div.content > div.mod-panel > div.bd > div.table > table > tbody > tr:nth-child(1) > td:nth-child(1)"#标记路径
results = r.html.find(sel)#查找列表
print(results[0].text)#输出结果