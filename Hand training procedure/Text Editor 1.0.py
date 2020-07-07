 # -*- coding: gbk -*-

#函数 修改内容
def Revised_content(file):
    old_str=input('请输入你想修改的内容：'+'\n')
    new_str=input('你想将内容改为：'+'\n')
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)
    print("修改后的txt文件如下：")
    with open(file,encoding="utf-8") as file_object:
        contents = file_object.read()
        print(contents)

#函数 添加内容        
def Add_content(file):
	str_add=input("请输入你要添加的内容:")
	with open(file,'a',encoding="utf-8") as file_object:
		print('\n')
		file_object.write('\n'+str_add)
	print('\n')	
	print("添加后的txt文件如下：")
	with open(file,encoding="utf-8") as file_object:
		contents = file_object.read()
		print(contents)

#打开txt文件
file_path=input("请输入你需要打开的文件路径:")
print('\n'+file_path+'的内容如下：')
with open(file_path,encoding="utf-8") as file_object:
	contents = file_object.read()
	print(contents)
	print('\n')

#选择服务类型
number=input('你想要做什么？\n添加内容请输入1\n修改内容请输入2\n')

if number=='1':
	Add_content(file_path)
if number=='2':
	Revised_content(file_path)
