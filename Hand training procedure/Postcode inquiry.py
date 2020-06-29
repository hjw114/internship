from requests_html import HTMLSession
session=HTMLSession()
postcode=input("请输入邮编:")
url="https://www.ip138.com/post/search.asp?zip="+postcode+"&action=zip2area"
r=session.get(url)
sel="body > div > div.container > div.content > div.mod-panel > div.bd > div.table > table > tbody > tr:nth-child(1) > td:nth-child(1)"
results = r.html.find(sel)
print(results[0].text)