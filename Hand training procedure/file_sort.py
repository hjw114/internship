f=open('D:/test/m.txt')
result= []
iter_f=iter(f)     
for line in iter_f:
    result.append(line)
f.close()
result.sort()
f=open('D:/test/m.txt','w')
f.writelines(result)
f.close()
