import os,time
import json

def save_money(wallet, record, amount, comment):
    date = time.strftime("%Y-%m-%d")

    with open(wallet) as fobj:
        balance = json.load(fobj) + amount

    with open(wallet, 'w') as fobj:
        json.dump(balance, fobj)

    with open(record, 'a') as fobj:
        fobj.writelines(date + '  N/A  ' + str(amount) + '  ' + str(balance) + '  '  + comment + "\n")


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


def query_money(wallet, record):
    print( 'date         cost   save   balance   comment\n')
    with open(record) as fobj:
        for line in fobj:
            print(line)
    with open(wallet) as fobj:
        print("New Balance: " + str(json.load(fobj)))

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
        choice = input("(0) save money  (1) spend money  (2) query detail  (3) quit  Please input your choice(0/1/2/3):")

        if choice not in '0123':
            print("Invalid input, Try again.")
            continue

        if choice in '0':
            amount = int(input("Amount: "))
            comment = input("Comment: ")
            save_money(w_file, r_file, amount, comment)
            continue

        if choice in '1':
            amount = int(input("Amount: "))
            comment = input("Comment: ")
            cost_money(w_file, r_file, amount, comment)
            continue

        if choice in '2':
            query_money(w_file, r_file)
            continue

        if choice == '3':
            break



if __name__ == '__main__':

    print(show_menu())