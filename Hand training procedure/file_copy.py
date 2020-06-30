path = 'D:\test\\'  
fp = open(path + 'm.txt')  
a = fp.readlines()  
a = [x.split('\t') for x in a]  
a = [[x[0],x[1].replace('\n','')] for x in a]  
print (a)  
fp.close()  
  
b = [[int(x[0]), int(x[1])] for x in a]  
b.sort()  
b = [str(x[0]) + '\t' + str(x[1]) + '\n' for x in b]  
fp = open(path+'n.txt', 'w')  
fp.writelines(b)  
fp.close()  
print (b)  
