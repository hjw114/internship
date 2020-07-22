#coding=gbk
#学生成绩管理器——记录一个班级的学生（创建一个Student类，记录他们的名字、平均分和考试分数）
#学生ID为九位数字 目前存在一个小bug，学生姓名两个字的成绩与三个字的成绩不能对齐 运行该程序可能需要在目录下新建一个students.txt
import os
import re
import numpy as np

class Student: #定义一个学生类
    def __init__(self):
        self.name = ''
        self.ID =''
        self.score1 = 0
        self.score2 = 0
        self.ave = 0


def searchByID(stulist, ID): #按学号查找看是否学号已经存在
    for item in stulist:
        if item.ID == ID:
            return True

def Add(stulist,stu): #添加一个学生信息
    if searchByID(stulist, stu.ID) == True:
        print("学号已经存在！")
        return False
    stulist.append(stu)
    print (stu.name,stu.ID, stu.score1, stu.score2, stu.ave);
    print ("是否要保存学生信息？")
    nChoose = input("Choose Y/N")
    if nChoose == 'Y' or nChoose == 'y':
        file_object = open("students.txt", "a")
        file_object.write(stu.ID)
        file_object.write(" ")
        file_object.write(stu.name)
        file_object.write(" ")
        file_object.write(str(stu.score1))
        file_object.write(" ")
        file_object.write(str(stu.score2))
        file_object.write(" ")
        file_object.write(str(stu.ave))
        file_object.write("\n")
        file_object.close()
        print ("保存成功！")

def Search(stulist, ID): #搜索一个学生信息
    print ("学号             姓名        平时分    测试分    平均分")
    count = 0
    for item in stulist:
        if item.ID == ID:
            print (item.ID, '\t' ,item.name,'\t', item.score1,'\t',item.score2, '\t',item.ave)
            break
        count = 0
    if count == len(stulist):
        print ("没有该学生学号！")

def Del(stulist, ID): #删除一个学生信息
    count = 0
    for item in stulist:
        if item.ID == ID:
            stulist.remove(item)
            print ("删除成功！")
            break
        count +=1
    # if count == len(stulist):
    #   print "没有该学生学号！"
    file_object = open("students.txt", "w")
    for stu in stulist:
        print (stu.ID, stu.name, stu.score1,stu.score2,  stu.sum)
        file_object.write(stu.ID)
        file_object.write(" ")
        file_object.write(stu.name)
        file_object.write(" ")
        file_object.write(str(stu.score1))
        file_object.write(" ")
        file_object.write(str(stu.score2))
        file_object.write(" ")
        file_object.write(str(stu.ave))
        file_object.write("\n")
        file_object.close()
    #   print "保存成功！"
    file_object.close()
    
def Change(stulist, ID):
    count = 0
    for item in stulist:
        if item.ID == ID:
            stulist.remove(item)
            file_object = open("students.txt", "w")
            for stu in stulist:
                #print li.ID, li.name, li.score
                file_object.write(stu.ID)
                file_object.write(" ")
                file_object.write(stu.name)
                file_object.write(" ")
                file_object.write(str(stu.score1))
                file_object.write(" ")
                file_object.write(str(stu.score2))
                file_object.write(" ")
                file_object.write(str(stu.sum))
                file_object.write("\n")
            #   print "保存成功！"
            file_object.close()
            stu = Student()
            stu.name = input("请输入学生的姓名")
            while True:
                stu.ID = input("请输入学生的ID")
                p = re.compile('^[0-9]{3}$')
                if p.match(stu.ID):
                    break
                else:
                    print ("输入的有错误！")
            while True:
                stu.score1 = int(input("请输入学生平时分"))
                if stu.score1 <= 100 and stu.score1 > 0 :
                    break
                else:
                    print ("输入的学生成绩有错误！")
            while True:
                stu.score2 = int(input("请输入学生测验分"))
                if stu.score2 <= 100 and stu.score2 > 0 :
                    break
                else:
                    print ("输入的学生成绩有错误！")
            stu.ave = (stu.score1 + stu.score2)/2
            Add(stulist,stu)
            
def display(stulist): #显示所有学生信息
    print ("学号             姓名        平时分    测试分    平均分")
    for item in stulist:
        print (item.ID, '\t' ,item.name,'\t', item.score1,'\t',item.score2, '\t',item.ave)


def insertSort(a, stulist):  
    for i in range(len(a)-1):  
        #print a,i    
        for j in range(i+1,len(a)):  
            if a[i]<a[j]:  
                temp = stulist[i]  
                stulist[i] = stulist[j]  
                stulist[j] = temp  
    #return a 

def Init(stulist):  #初始化函数
    print ("初始化......")
    file_object = open('students.txt', 'r')
    for line in file_object:
        stu = Student()
        line = line.strip("\n")
        s = line.split(" ")
        stu.ID = s[0]
        stu.name = s[1]
        stu.score1 = s[2]
        stu.score2 = s[3]
        stu.ave = s[4]
        stulist.append(stu)
    file_object.close()
    print ("初始化成功！")
    main()

def main(): #主函数 该程序的入口函数
    while True:
        print ("*********************")
        print ("--------菜单---------")
        print ("增加学生信息--------1")
        print ("查找学生信息--------2")
        print ("删除学生信息--------3")
        print ("修改学生信息--------4")
        print ("所有学生信息--------5")
        print ("退出程序------------0")
        print ("*********************")

        nChoose = input("请输入你的选择：")
        if nChoose == "1":
            stu = Student()
            stu.name = input("请输入学生的姓名")
            while True:
                stu.ID = input("请输入学生的ID")
                p = re.compile('^[0-9]{9}$')
                if p.match(stu.ID):
                    break
                else:
                    print ("输入的有错误！")
            while True:
                stu.score1 = int(input("请输入学生的平时分"))
                if stu.score1 <= 100 and stu.score1 > 0 :
                    break
                else:
                    print ("输入的学生成绩有错误！")
            while True:
                stu.score2 = int(input("请输入学生的测验分"))
                if stu.score2 <= 100 and stu.score2 > 0 :
                    break
                else:
                    print ("输入的学生成绩有错误！")
            stu.ave=(stu.score1 + stu.score2)/2
            Add(stulist,stu)

        if nChoose == '2':
            ID = input("请输入学生的ID")
            Search(stulist, ID)

        if nChoose == '3':
            ID = input("请输入学生的ID")
            Del(stulist, ID)
        if nChoose == '4':
            ID = input("请输入学生的ID")
            Change(stulist, ID)

        if nChoose == '5':
            display(stulist)

        if nChoose == '0':
            break

if __name__ == '__main__':
    stulist =[]
Init(stulist)

