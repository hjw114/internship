#初始化Key取值表
char_table = "23456789ABCDEFGHJKLMNPQRSTUVWXYZ"


def CdKey_build(num):
    result = ""

    if abs(len(num) - 3) > 0.5:
        result = "输入的不是一个三位数，请重新运行程序并输入正确的数字"
    else:
        try:
            #将输入的数的各个位分别转化为16位的二进制表示后组合成48位二进制数
            bin_num1 = str(bin(int(num[0])))[2:]
            bin_num2 = str(bin(int(num[1])))[2:]
            bin_num3 = str(bin(int(num[2])))[2:]
        except (ValueError, IndexError):
            print("输入的不是一个三位数，请重新运行程序并输入正确的数字")
        else:
            bin_48 = bin_num1.zfill(16) + bin_num2.zfill(16) + bin_num3.zfill(16)

            for i in range(20):
                #形成CD-Key格式
                if i % 5 == 0 and i != 0:
                    result += '-'
                #对48位二进制数从低到高每次取5位组成新的数字，并从取值表选择对应值
                result += char_table[int(bin_48[-5:],2)]
                bin_48 = bin_48[-5:] + bin_48[:-5]

    return result


# 主函数
if __name__ == '__main__':
    num = input("请输入一个任意三位数（000-999）: ")
    print(CdKey_build(num))

    input()# 防止程序直接运行时闪退，无意义