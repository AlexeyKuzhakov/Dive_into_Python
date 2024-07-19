
from math import pi
import decimal

decimal.getcontext().prec = 42
PI = decimal.Decimal(pi)

diameter = decimal.Decimal(input('Введите диаметр: '))

while diameter > 1000:
    print('Диаметр не должен превышать 1000')
    diameter = decimal.Decimal(input('Введите диаметр: '))

square = PI * (diameter / 2) ** 2
length = PI * diameter

print(f'Площвдь равна {square}\nДлина равна {length= }')