#coding=gbk
import sqlite3

DB_Name='test.db'

# �������ݿ⣬�������������ڵ�ǰĿ¼����
conn = sqlite3.connect(DB_Name)

print('�������ݿ�%s�ɹ�'%(DB_Name))

