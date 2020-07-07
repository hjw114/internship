#coding=gbk
import sqlite3

DB_Name='test.db'

# 连接数据库，如果不存在则会在当前目录创建
conn = sqlite3.connect(DB_Name)

print('连接数据库%s成功'%(DB_Name))

