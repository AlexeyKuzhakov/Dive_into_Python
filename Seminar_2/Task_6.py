
import decimal

decimal.getcontext().prec = 2
MULTIPLICITY = 50
PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
PERCENT_BONUS = decimal.Decimal(3) / decimal.Decimal(100)
COUNT_PERC = 3
MIN_LIMIT = decimal.Decimal(30)
MAX_LIMIT = decimal.Decimal(600)
PERCENT_RICHNESS = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_AMOUNT = 5_000_000
CMD_DEPOSIT = '1'
CMD_WITHDRAW = '2'
CMD_EXIT = '3'


balance = 0
operations = 0

while True:
    action = input(
        f'пополнить - {CMD_DEPOSIT}\n'
        f'снять - {CMD_WITHDRAW}\n'
        f'выход - {CMD_EXIT}\n'
        f'ведите действие: '
    )
    if balance > RICHNESS_AMOUNT and action != 3:
        sum_percent = balance * PERCENT_RICHNESS
        balance -= sum_percent
        print(f'Вычтен налог на богатство в размере {sum_percent}')
        print(f'Текущий баланс {balance}')
    if action == '1' or action == '2':
        amount = 1
        while amount % MULTIPLICITY != 0:
            amount = int(input(f'Введите сумму кратную {MULTIPLICITY}: '))
        if action == '1':
            operations += 1
            balance += amount
            # print(f'Текущий баланс {balance}')
        else:
            comission = amount * PERCENT
            if comission < MIN_LIMIT:
                comission = MIN_LIMIT
            elif comission > MAX_LIMIT:
                comission = MAX_LIMIT
            if comission + amount > balance:
                print('На балансе недостаточно средств')
                print(f'Сумма снятия {amount}, комиссия {comission}, общая сумма {amount + comission}')
                # print(f'Текущий баланс {balance}')
            else:
                operations += 1
                balance -= (amount + comission)
            print(f'Сумма снятия {amount}, комиссия {comission}, общая сумма {amount + comission}')
            # print(f'Текущий баланс {balance}')
        if operations % COUNT_PERC == 0:
            bonus_sum = balance * PERCENT_BONUS
            balance += bonus_sum
            print(f'Сумма бонуса {bonus_sum}')
            # print(f'Текущий баланс {balance}')
        print(f'Текущий баланс {balance}')
    elif action == '3':
        break
    else:
        print('Введена неверная команда')