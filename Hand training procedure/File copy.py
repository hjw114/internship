i=1
position0=input("请输入文件位置:")
with open(position0,encoding="utf-8") as file0:#确认文件无误
    contents=file0.read()#读取文件
    print(contents)
judge=input("请输入Y|F")
if(judge=="Y"):
    x=input("请输入复制次数:")
    position1=input("请输入复制位置:")
    while i<=int(x):#多次复制
        with open(position1+"\copy"+str(i)+".txt","w",encoding="utf-8") as file:
            file.write(contents)#写入文件
            i+=1
else:
    print("回去重新找文件！")