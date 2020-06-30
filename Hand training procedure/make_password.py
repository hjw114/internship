import hashlib

# 原密码
str = 'I like you'

# 创建md5对象
hl = hashlib.md5()
hl.update(str.encode(encoding='utf-8'))
print('MD5加密前为 ：' + str)
print('MD5加密后为 ：' + hl.hexdigest())
