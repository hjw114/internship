#coding=gbk
#������������Ϸ��������һ��Ӣ��������Ϸ�����������ǽ�һ��Ӣ�ﵥ�ʵĵ�һ���������ص���ĸ�ƶ�����β���Ҽ��Ϻ�׺-ay��Ʃ�硰banana�����ɡ�anana-bay������
import re
x = input('please enter your words:')
def game_pigwords(x):
    reg = r'[^aeiou]'
    pattern = re.compile(reg)
    f_word = re.sub(pattern,'',x,count=1)                     # �ÿ�ֵ�����һ��������ĸ����ȡȥ��һ����ĸ���ַ���
    the_letter_objective = re.search(pattern,x)      # search()��match()���ص���һ������
    single_word = the_letter_objective.group()       # ���ö���ķ������� Objective.group()
    the_pig_word = f_word + single_word +'��ay'
    return the_pig_word
    #return f_word,single_word,the_pig_word
    #print(fw)
print(game_pigwords(x))
