#coding=gbk
from PIL import Image,ImageDraw
 
def addText(img,string):
  size = img.size
  width = size[0] - 50
  high = size[1] - 60
  lenth = len(string)*5
  draw = ImageDraw.Draw(img)
  draw.text((width-lenth,high),string,fill='black')
  oriImg.show()
  oriImg.save(path)
 
 
path = input("Please input the image file with path:")

string1=input('�Բ���qaq��������Ŀǰ���ܽ�������'+'\n'+'���������������')
string2=input('\n'+'������������գ�')
string3=input('\n'+'��������ĸ��ԣ�')
string=string1+'\n'+string2+'\n'+string3
 
try:
  print("path: "+path)
  oriImg = Image.open(path)
  addText(oriImg,string)
except IOError:
  print("can't' open the file,check the path again")
  newImg = Image.new('RGBA',(320,240),'white')
  newImg.save(path)
