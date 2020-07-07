 # -*- coding: gbk -*-

def xgnr(file):
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
        
    print("增添后的txt文件如下：")
    with open(file,encoding="utf-8") as file_object:
        contents = file_object.read()
        print(contents)
        
def xznr(file):
	str_add=input("请输入你要新添的内容:")
	with open(file,'a',encoding="utf-8") as file_object:
		print('\n')
		file_object.write('\n'+str_add)
	print('\n')	
	print("增添后的txt文件如下：")
	with open(file,encoding="utf-8") as file_object:
		contents = file_object.read()
		print(contents)
file_path=input("请输入你需要打开的文件路径:")

print('\n'+file_path+'的内容如下：')
with open(file_path,encoding="utf-8") as file_object:
	contents = file_object.read()
	print(contents)
	print('\n')

number=input('你想要做什么？\n新增内容请输入1\n修改内容请输入2\n')
if number=='1':
	xznr(file_path)
if number=='2':
	xgnr(file_path)
