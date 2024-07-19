
LOWER_LIMIT = 1
UPPER_LIMIT = 999
ONE = 1
TEN = 10
HUNDRED = 100
num = LOWER_LIMIT - ONE

while num < LOWER_LIMIT or num > UPPER_LIMIT:
    num = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))

if num < TEN:
    result = f'Число {num} - цифра. Ее квадрат = {num * num}'
elif num < HUNDRED:
    f_num = num // TEN
    s_num = num % TEN
    result = f'Число {num} двузначное. Произведение цифр = {f_num * s_num}'
else:
    f_num = num // HUNDRED
    s_num = num // TEN % TEN
    t_num = num % TEN
    result = f'Число {num} трехзначное. Зеракальное отображение = {t_num * HUNDRED + s_num * TEN + f_num}'

print(result)