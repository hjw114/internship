#coding=gbk
import turtle
import threading
#海龟图——创建一个20*20的格子，用命令让一只海龟在格子上画线。可以前进、左转、右转，拿起或放下笔等等。

#创建画线的海龟
t = turtle.Pen()   

#创建20*20的格子,以15个像素点为格子边长
def creatScreen():    
	#构建20*20的正方形，格子的线为黑色   
	t.forward(20*15)    
	t.right(90)    
	t.forward(20*15)    
	t.right(90)    
	t.forward(20*15)    
	t.right(90)    
	t.forward(20*15)    
	#绘制竖制的19条线    
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
			
#前进
def forword(distance):   
	 t.forward(15*distance) 

#向左转
def left():    
	t.left(90) 

#向右转
def right():    
	t.right(90) 
	
#拿起画笔
def up():    
	t.up() 
	
#放下画笔
def down():    
	t.down() 
	
#主函数
def main():    
	creatScreen()
	t.color("green")   #海龟画的线改为绿色
	print("请输入对海龟的命令,以End为退出标志"+"\n"+"1代表前进，2代表海龟向左旋转90度，3代表海龟向右旋转90度，4代表海龟拿起画笔，5代表海龟放下画笔"+"\n")    
	comand = input()    
	while comand!="End" :        
		if comand == "1":            
			print("前进格子数目")            
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
	

