def Pig_Latin(s):
    s=s.lower()
    if s[0] in 'aeiou':
        vowel_begin = True
    else:
        vowel_begin = False
    if vowel_begin:
        s = s+'hay'
    #以元音字母开始，则在单词末尾加入“hay”
    if s[0]=='q' and s[1] =='u':
        s =s[2:]+'quay'
    #以‘q’字母开始，并且后面有个字母‘u’，将“qu”移动到单词末尾加入“ay”
    end = 0
    for i in range(len(s)):
        if s[i] in 'aeiou' or (i>0 and s[i]=='y'):
            end = i
            break
    s=s[end:]+s[:end]+'ay'
    #以辅音字母开始，所有连续的辅音字母一起移动到单词末尾加入“ay”
    return s
def transfer_main(str):
    s = str.split()
    result = []
    for i in s:
        result.append(Pig_Latin(i))
    new_s=' '.join(result)
    return new_s
print(transfer_main('the champion belongs to Wuhan Estarpro'))

