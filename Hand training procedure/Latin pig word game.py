#coding=gbk
#拉丁猪文字游戏——这是一个英语语言游戏。基本规则是将一个英语单词的第一个辅音音素的字母移动到词尾并且加上后缀-ay（譬如“banana”会变成“anana-bay”）。
import re
x = input('please enter your words:')
def game_pigwords(x):
    reg = r'[^aeiou]'
    pattern = re.compile(reg)
    f_word = re.sub(pattern,'',x,count=1)                     # 用空值替代第一个辅音字母，获取去除一个字母的字符串
    the_letter_objective = re.search(pattern,x)      # search()和match()返回的是一个对象。
    single_word = the_letter_objective.group()       # 调用对象的方法则是 Objective.group()
    the_pig_word = f_word + single_word +'—ay'
    return the_pig_word
    #return f_word,single_word,the_pig_word
    #print(fw)
print(game_pigwords(x))
