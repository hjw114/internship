 # -*- coding: gbk -*-

def xgnr(file):
    old_str=input('�����������޸ĵ����ݣ�'+'\n')
    new_str=input('���뽫���ݸ�Ϊ��'+'\n')
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)
        
    print("������txt�ļ����£�")
    with open(file,encoding="utf-8") as file_object:
        contents = file_object.read()
        print(contents)
        
def xznr(file):
	str_add=input("��������Ҫ���������:")
	with open(file,'a',encoding="utf-8") as file_object:
		print('\n')
		file_object.write('\n'+str_add)
	print('\n')	
	print("������txt�ļ����£�")
	with open(file,encoding="utf-8") as file_object:
		contents = file_object.read()
		print(contents)
file_path=input("����������Ҫ�򿪵��ļ�·��:")

print('\n'+file_path+'���������£�')
with open(file_path,encoding="utf-8") as file_object:
	contents = file_object.read()
	print(contents)
	print('\n')

number=input('����Ҫ��ʲô��\n��������������1\n�޸�����������2\n')
if number=='1':
	xznr(file_path)
if number=='2':
	xgnr(file_path)
