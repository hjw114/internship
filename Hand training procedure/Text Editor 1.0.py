 # -*- coding: gbk -*-

#���� �޸�����
def Revised_content(file):
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
    print("�޸ĺ��txt�ļ����£�")
    with open(file,encoding="utf-8") as file_object:
        contents = file_object.read()
        print(contents)

#���� �������        
def Add_content(file):
	str_add=input("��������Ҫ��ӵ�����:")
	with open(file,'a',encoding="utf-8") as file_object:
		print('\n')
		file_object.write('\n'+str_add)
	print('\n')	
	print("��Ӻ��txt�ļ����£�")
	with open(file,encoding="utf-8") as file_object:
		contents = file_object.read()
		print(contents)

#��txt�ļ�
file_path=input("����������Ҫ�򿪵��ļ�·��:")
print('\n'+file_path+'���������£�')
with open(file_path,encoding="utf-8") as file_object:
	contents = file_object.read()
	print(contents)
	print('\n')

#ѡ���������
number=input('����Ҫ��ʲô��\n�������������1\n�޸�����������2\n')

if number=='1':
	Add_content(file_path)
if number=='2':
	Revised_content(file_path)
