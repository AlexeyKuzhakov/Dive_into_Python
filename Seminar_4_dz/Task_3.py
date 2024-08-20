# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

from datetime import date

bank = 0
count = 0
percent_take = 0.015
percent_add = 0.03
percent_tax = 0.01

def add_bank(cash: float) -> None:
    global bank
    global count
    bank += cash
    count += 1
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("Начислены 3% в размере: ", percent_add * bank, "y.e.")

def take_bank(cash: float) -> None:
    global bank
    global count
    bank -= cash
    count += 1

    if cash * percent_take < 30:
        bank -= 30
        print("Списаны 1.5% за cash: ", 30, "y.e.")
    elif cash * percent_take > 600:
        bank -= 600
        print("списаны 1.5% за cash: ", 600, "y.e.")
    else:
        bank -= cash * percent_take
        print("Списаны 1.5% за cash: ", cash * percent_take, "y.e.")
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("Начислены 3% в размере: ", percent_add * bank, "y.e.")


def exit_bank():
    print("Рады видеть вас снова!\n")
    exit()

def check_bank() -> int:
    while True:
        cash = int(input("Введите сумму операции кратно 50\n"))
        if cash % 50 == 0:
            return cash

list_operation = []

while True:
    action = input("1 - снять деньги\n2 - пополнить\n3 - баланс\n4 - вывести историю операций\n5 - выйти\n")

    if action == '1':
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("Списано 10% налог на богатство: ", bank * percent_tax, "y.e.")
        cash = check_bank()
        if cash < bank:
            take_bank(cash)

            list_operation.append([str(date.today()), -1 * cash])
        else:
            print("Нельзя снять >" , bank, "y.e.")
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("Списано 10% налог на богатство: ", bank * percent_tax, "y.e.")
        print("Баланс = ", bank, "y.e.")
    elif action == '2':
        cash = check_bank()
        add_bank(cash)
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("Списано 10% налог на богатство: ", bank * percent_tax, "y.e.")
        print("Баланс = ", bank, "y.e.")

        list_operation.append([str(date.today()), cash])

    elif action == '3':
        print("Баланс = ", bank, "y.e.")
    elif action == '4':
        print(list_operation)
    else:
        exit_bank()