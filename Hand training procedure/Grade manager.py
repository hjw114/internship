#coding=gbk
#ѧ���ɼ�������������¼һ���༶��ѧ��������һ��Student�࣬��¼���ǵ����֡�ƽ���ֺͿ��Է�����
#ѧ��IDΪ��λ���� Ŀǰ����һ��Сbug��ѧ�����������ֵĳɼ��������ֵĳɼ����ܶ��� ���иó��������Ҫ��Ŀ¼���½�һ��students.txt
import os
import re
import numpy as np

class Student: #����һ��ѧ����
    def __init__(self):
        self.name = ''
        self.ID =''
        self.score1 = 0
        self.score2 = 0
        self.ave = 0


def searchByID(stulist, ID): #��ѧ�Ų��ҿ��Ƿ�ѧ���Ѿ�����
    for item in stulist:
        if item.ID == ID:
            return True

def Add(stulist,stu): #���һ��ѧ����Ϣ
    if searchByID(stulist, stu.ID) == True:
        print("ѧ���Ѿ����ڣ�")
        return False
    stulist.append(stu)
    print (stu.name,stu.ID, stu.score1, stu.score2, stu.ave);
    print ("�Ƿ�Ҫ����ѧ����Ϣ��")
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
        print ("����ɹ���")

def Search(stulist, ID): #����һ��ѧ����Ϣ
    print ("ѧ��             ����        ƽʱ��    ���Է�    ƽ����")
    count = 0
    for item in stulist:
        if item.ID == ID:
            print (item.ID, '\t' ,item.name,'\t', item.score1,'\t',item.score2, '\t',item.ave)
            break
        count = 0
    if count == len(stulist):
        print ("û�и�ѧ��ѧ�ţ�")

def Del(stulist, ID): #ɾ��һ��ѧ����Ϣ
    count = 0
    for item in stulist:
        if item.ID == ID:
            stulist.remove(item)
            print ("ɾ���ɹ���")
            break
        count +=1
    # if count == len(stulist):
    #   print "û�и�ѧ��ѧ�ţ�"
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
    #   print "����ɹ���"
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
            #   print "����ɹ���"
            file_object.close()
            stu = Student()
            stu.name = input("������ѧ��������")
            while True:
                stu.ID = input("������ѧ����ID")
                p = re.compile('^[0-9]{3}$')
                if p.match(stu.ID):
                    break
                else:
                    print ("������д���")
            while True:
                stu.score1 = int(input("������ѧ��ƽʱ��"))
                if stu.score1 <= 100 and stu.score1 > 0 :
                    break
                else:
                    print ("�����ѧ���ɼ��д���")
            while True:
                stu.score2 = int(input("������ѧ�������"))
                if stu.score2 <= 100 and stu.score2 > 0 :
                    break
                else:
                    print ("�����ѧ���ɼ��д���")
            stu.ave = (stu.score1 + stu.score2)/2
            Add(stulist,stu)
            
def display(stulist): #��ʾ����ѧ����Ϣ
    print ("ѧ��             ����        ƽʱ��    ���Է�    ƽ����")
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

def Init(stulist):  #��ʼ������
    print ("��ʼ��......")
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
    print ("��ʼ���ɹ���")
    main()

def main(): #������ �ó������ں���
    while True:
        print ("*********************")
        print ("--------�˵�---------")
        print ("����ѧ����Ϣ--------1")
        print ("����ѧ����Ϣ--------2")
        print ("ɾ��ѧ����Ϣ--------3")
        print ("�޸�ѧ����Ϣ--------4")
        print ("����ѧ����Ϣ--------5")
        print ("�˳�����------------0")
        print ("*********************")

        nChoose = input("���������ѡ��")
        if nChoose == "1":
            stu = Student()
            stu.name = input("������ѧ��������")
            while True:
                stu.ID = input("������ѧ����ID")
                p = re.compile('^[0-9]{9}$')
                if p.match(stu.ID):
                    break
                else:
                    print ("������д���")
            while True:
                stu.score1 = int(input("������ѧ����ƽʱ��"))
                if stu.score1 <= 100 and stu.score1 > 0 :
                    break
                else:
                    print ("�����ѧ���ɼ��д���")
            while True:
                stu.score2 = int(input("������ѧ���Ĳ����"))
                if stu.score2 <= 100 and stu.score2 > 0 :
                    break
                else:
                    print ("�����ѧ���ɼ��д���")
            stu.ave=(stu.score1 + stu.score2)/2
            Add(stulist,stu)

        if nChoose == '2':
            ID = input("������ѧ����ID")
            Search(stulist, ID)

        if nChoose == '3':
            ID = input("������ѧ����ID")
            Del(stulist, ID)
        if nChoose == '4':
            ID = input("������ѧ����ID")
            Change(stulist, ID)

        if nChoose == '5':
            display(stulist)

        if nChoose == '0':
            break

if __name__ == '__main__':
    stulist =[]
Init(stulist)

