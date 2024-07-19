#3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
#Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
#Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

LOWER_LIMIT = 0
UPPER_LIMIT = 100000
EXEPTION = 1

num = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
if num < LOWER_LIMIT or num > UPPER_LIMIT:
    result = f'Число {num} не входит в указанный диапазон'
elif num == LOWER_LIMIT or num == EXEPTION:
    result = f'Число {num} не является ни простыми, ни составным'
else:
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count <= 2:
        result = f'Число {num} является простым'
    else:
        result = f'Число {num} является составным'

print(result)

