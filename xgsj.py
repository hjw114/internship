#coding=gbk

import sqlite3 
DB_Name = 'test.db'
# �������ݿ⣬�������������ڵ�ǰĿ¼����
conn = sqlite3.connect(DB_Name)
try:    
	# �����α�    
	cursor = conn.cursor()
	    
	# ��ѯ���ݵ�SQL���    
	SELECT_SQL = '''          
	SELECT * FROM STUDENT;          
	'''    
	
	# �޸����ݵ�SQL���    
	UPDATE_SQL = '''             
	UPDATE STUDENT SET SNAME='%s' WHERE SNO='%s'             
	''' % ('�', '2016081111')     
	
	# �޸�ǰ    print('�޸�ǰ')    
	cursor.execute(SELECT_SQL)    
	for row in cursor.fetchall():        
		print(row)    
		
	# �޸�����    
	cursor.execute(UPDATE_SQL)    
	
	# �ύ�����ݿ�    
	conn.commit()     
	
	# �޸ĺ�    
	print('�޸ĺ�')    
	cursor.execute(SELECT_SQL)    
	for row in cursor.fetchall():        
		print(row)
except Exception as e:    
	print(e)    
	print('�޸�����ʧ��')
finally:    
	# �ر����ݿ�    
	conn.close()

