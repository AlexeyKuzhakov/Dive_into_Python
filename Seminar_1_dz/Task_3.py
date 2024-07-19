#4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
#Программа должна подсказывать “больше” или “меньше” после каждой попытки.
#Для генерации случайного числа используйте код:
#from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)


from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
attempt = 10
num = randint(LOWER_LIMIT, UPPER_LIMIT)


while attempt > 0:
    print(f'У вас {attempt} попыток')
    attempt -= 1

    user_num = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
    if num == user_num:
        print(f'Вы угадали, программа загадала число: {num}')
        break
    elif num < user_num:
        print(f'Вы не угадали, программа загадала число меньше чем {user_num}')
    elif num > user_num:
        print(f'Вы не угадали, программа загадала число больше чем {user_num}')

else:
    print(f'Исчерпаны все попытки, верное число: {num}')

