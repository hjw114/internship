def String(strString):

    """
    统计元音字母——输入一个字符串，统计处其中元音字母的数量。
    更复杂点的话统计出每个元音字母的数量。
    """
    # 元音字母总个数
    num = 0
    # 每个元音字母的数量
    num_a = 0
    num_e = 0
    num_i = 0
    num_o = 0
    num_u = 0
    for t in strString:
        # 避免忽视大写字母
        i = t.lower()
        # 统计出元音字母的总数量
        if i in ['a', 'e', 'i', 'o', 'u']:
            num += 1
        # 统计出每个元音字母的数量
        if i == 'a':
            num_a += 1
        elif i == 'e':
            num_e += 1
        elif i == 'i':
            num_i += 1
        elif i == 'o':
            num_o += 1
        elif i == 'u':
            num_u += 1
    print("元音字母总个数是:%s" % num)
    print("其中a有%s个,e有%s个,i有%s个,o有%s个,u有%s个" %\
    (str(num_a), str(num_e), str(num_i), str(num_o), str(num_u)))

String('Hello everone Good Morning Today is A Sunny Day')

