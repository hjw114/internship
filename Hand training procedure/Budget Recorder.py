import os,time
import json

# 存入
def save_money(wallet, record, amount, comment):
    date = time.strftime("%Y-%m-%d")

    with open(wallet) as fobj:
        balance = json.load(fobj) + amount

    with open(wallet, 'w') as fobj:
        json.dump(balance, fobj)

    with open(record, 'a') as fobj:
        fobj.writelines(date + '  N/A  ' + str(amount) + '  ' + str(balance) + '  '  + comment + "\n")

# 支出
def cost_money(wallet, record, amount, comment):
    date = time.strftime("%Y-%m-%d")

    with open(wallet) as fobj:
        balance = json.load(fobj) - amount
    if balance < 0:
        print("余额不足，请先存钱或进行其他操作！")
    else:
        with open(wallet, 'w') as fobj:
            json.dump(balance, fobj)

        with open(record, 'a') as fobj:
            fobj.writelines(date + '  ' + str(amount) + '  N/A  '  + str(balance) + '  '  + comment)

# 查看明细
def query_money(wallet, record):
    print( 'date         cost   save   balance   comment\n')
    with open(record) as fobj:
        for line in fobj:
            print(line)
    with open(wallet) as fobj:
        print("New Balance: " + str(json.load(fobj)))

# 开始目录
def show_menu():
    w_file = 'wallet.txt'
    r_file = 'record.txt'

    if not os.path.isfile(w_file):
        with open(w_file, 'w') as fobj:
            json.dump(0, fobj)
    if not os.path.isfile(r_file):
        with open(r_file, 'w') as fobj:
            json.dump('',fobj)

    while True:
        choice = input("(0) 退出  (1) 存入  (2) 支出  (3) 这段时间内财务明细    Please input your choice(0/1/2/3):")
        if choice in '':
            print("求求你输入点东西")
            continue

        if choice in '1':
            amount = int(input("Amount: "))
            comment = input("Comment: ")
            save_money(w_file, r_file, amount, comment)
            continue

        elif choice in '2':
            amount = int(input("Amount: "))
            comment = input("Comment: ")
            cost_money(w_file, r_file, amount, comment)
            continue

        elif choice in '3':
            query_money(w_file, r_file)
            continue
        
        elif choice in '0':
            break
        
        else:
            print("Invalid input, Try again.")
            continue


# 主函数
if __name__ == '__main__':

    print(show_menu())
    print("记录文件已保存在程序运行目录下")
