#coding=gbk

#create_table_sqlite3.py �������ݿ��
import sqlite3 
DB_Name = 'test.db'
Table_Name = 'STUDENT'

# �������ݿ⣬�������������ڵ�ǰĿ¼����
conn = sqlite3.connect(DB_Name)
try:    
	# �����α�    
	cursor = conn.cursor()
	    
	# ����STUDENT���SQL��䣬Ĭ�ϱ���ΪUTF-8
	SQL = '''      
		CREATE TABLE %s (        
		SNO CHAR(10),        
		SNAME VARCHAR(20) NOT NULL,        
		PRIMARY KEY(SNO)    )        
		''' % (Table_Name)    
		
	# �������ݿ��    
	cursor.execute(SQL)     
	
	# �ύ�����ݿ�    
	conn.commit()   
	 
	print('�������ݿ��%s�ɹ�' % (Table_Name))
except Exception as e:   
	print(e)    
	
	# �ع�    
	conn.rollback()    
	print('�������ݿ��%sʧ��' % Table_Name)
finally:    
	# �ر����ݿ�    
	conn.close()

