#coding=gbk
import turtle
import threading
#����ͼ��������һ��20*20�ĸ��ӣ���������һֻ�����ڸ����ϻ��ߡ�����ǰ������ת����ת���������±ʵȵȡ�

#�������ߵĺ���
t = turtle.Pen()   

#����20*20�ĸ���,��15�����ص�Ϊ���ӱ߳�
def creatScreen():    
	#����20*20�������Σ����ӵ���Ϊ��ɫ   
	t.forward(20*15)    
	t.right(90)    
	t.forward(20*15)    
	t.right(90)    
	t.forward(20*15)    
	t.right(90)    
	t.forward(20*15)    
	#�������Ƶ�19����    
	i = 0    
	j = 0    
	while i<10 :        
		t.right(90)        
		t.forward(15)        
		t.right(90)        
		t.forward(20*15)        
		t.left(90)        
		t.forward(15)        
		t.left(90)        
		t.forward(20*15)        
		i = i+1    
	t.right(180)    
	while j<10 :        
		t.forward(15)        
		t.right(90)        
		t.forward(20*15)        
		t.left(90)        
		t.forward(15)        
		t.left(90)        
		t.forward(15*20)        
		t.right(90)        
		j = j+1  
			
#ǰ��
def forword(distance):   
	 t.forward(15*distance) 

#����ת
def left():    
	t.left(90) 

#����ת
def right():    
	t.right(90) 
	
#���𻭱�
def up():    
	t.up() 
	
#���»���
def down():    
	t.down() 
	
#������
def main():    
	creatScreen()
	t.color("green")   #���껭���߸�Ϊ��ɫ
	print("������Ժ��������,��EndΪ�˳���־"+"\n"+"1����ǰ����2������������ת90�ȣ�3������������ת90�ȣ�4���������𻭱ʣ�5��������»���"+"\n")    
	comand = input()    
	while comand!="End" :        
		if comand == "1":            
			print("ǰ��������Ŀ")            
			distance = int(input())            
			forword(distance)           
			comand = input()
		elif comand == "2":            
			left()            
			comand = input()		       
		elif comand == "3":            
			right()
			comand = input()          			       
		elif comand == "4":            
			up()
			comand = input()           			        
		elif comand == "5":            
			down()
			comand = input()           

if __name__ == '__main__':    
	main()
	

