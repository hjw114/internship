#coding=gbk
#��ѯ����
import sqlite3 
DB_Name = 'test.db'

# �������ݿ⣬�������������ڵ�ǰĿ¼����
conn = sqlite3.connect(DB_Name)
try:    
	# �����α�    
	cursor = conn.cursor()    
	
	# ��ѯ���ݵ�SQL���    
	SQL = '''          
		SELECT * FROM STUDENT;          
		'''    
		
	# ��ѯ����    
	cursor.execute(SQL)     
	
	# ��ȡһ������    
	one = cursor.fetchone()    
	print(one)     
	
	# ��ȡ��������    
	for row in cursor.fetchall():        
		print(row) 
		
except Exception as e:    
	print(e)    
	print('��ѯ����ʧ��')
	
finally:    
	# �ر����ݿ�    
	conn.close()
