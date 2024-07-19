
BIG_LEAP_YEAR = 400
SMALL_LEAP_YEAR = 4
LEARGE_NOT_BIG_YEAR = 100
MULTIPLE = 0
REFORM = 1582

year = int(input('Введите год: '))

if year < REFORM:
    result = f'Год {year} до ввода Григорианского календаря'
elif not year % BIG_LEAP_YEAR:
    result = f'Год {year} високосный'
elif not year % LEARGE_NOT_BIG_YEAR:
    result = f'Год {year}  не високосный'
elif not year % SMALL_LEAP_YEAR:
    result = f'Год {year} високосный'
else:
    result = f'Год {year}  не високосный'

print(result)