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


# �õ����ݿ����ӣ���Ϊ�涨���ݿ����ӺͲ���������ͳһ�߳�
def getConnection():
    conn = sqlite3.connect(r'D:\deskPicc\background.db')
    return conn


#���س���ʹ�õĴ���
def getStartTimes():
    conn = getConnection()
    cursor = conn.execute(r"select * from t_config")
    for i in cursor:
        times = i[0]
        times = int(times) + 1
        sql = "update t_config set start_times = {}".format(str(times))
        print(sql)
        conn.execute(sql)
        conn.commit()
    conn.close()
    return times - 1


#����url����
def insertInto(urls):
    conn = getConnection()
    for i in urls:
        sql = "insert into t_urls('url') values('{}')".format(i)
        conn.execute(sql)
        conn.commit()
        print(sql)
    conn.close()


def getUrls():
    conn = getConnection()
    sql = 'select * from t_urls'
    cursor = conn.execute(sql)
    urls = [i[0] for i in cursor]
    print('getUrls from db : ')
    print(urls)


    conn.commit()
    conn.close()
    return urls


def removeDb():
    conn = getConnection()
    sql1 = 'drop table t_config'
    sql2 = 'drop table t_urls'
    conn.execute(sql1)
    conn.execute(sql2)


    conn.commit()
    conn.close()

