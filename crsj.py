#coding=gbk
#�������ݿ⣬�������������ڵ�ǰĿ¼����
import sqlite3 
DB_Name = 'test.db'

conn = sqlite3.connect(DB_Name)
try:    
	# �����α�    
	cursor = conn.cursor()    
	
	# ��STUDENT��������ݵ�SQL���    
	SQL = '''          
		INSERT INTO STUDENT VALUES('2016081111','����'),('2016081112','����'),('2016081113','����');
	    '''    
	# ��������    
	cursor.execute(SQL)     
	
	# �ύ�����ݿ�    
	conn.commit()    
	print('�������ݵ���STUDENT�ɹ�')
except Exception as e:    
	print(e)    
	
	# �ع�    
	conn.rollback()    
	print('�������ݵ���STUDENTʧ��')
	
finally:    
	# �ر����ݿ�    
	conn.close()

