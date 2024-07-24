# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

from fractions import Fraction

fraction_first = input('Введите первую дробь в ввиде a/b: ')
fraction_second = input('Введите вторую дробь в ввиде a/b: ')

a_fraction_first, b_fraction_first = map(int, fraction_first.split('/'))
a_fraction_second, b_fraction_second = map(int, fraction_second.split('/'))
fract_sum = (a_fraction_first / b_fraction_first) + (a_fraction_second / b_fraction_second)
fract_mult = (a_fraction_first / b_fraction_first) * (a_fraction_second / b_fraction_second)
print(f'Сумма дробей {fraction_first} и {fraction_second} = {fract_sum}\n'
      f'Произведение дробей {fraction_first} и {fraction_second} = {fract_mult}')

print()
# С использованием модуля fraction
def fraction_sum_and_mult(fraction_first, fraction_second):
    fraction_1 = Fraction(fraction_first)
    fraction_2 = Fraction(fraction_second)
    fraction_sum = fraction_1 + fraction_2
    fraction_multiplication = fraction_1 * fraction_2
    return (f'Сумма дробей {fraction_first} и {fraction_second} = {fraction_sum}\n'
            f'Произведение дробей {fraction_first} и {fraction_second} = {fraction_multiplication}')
print(fraction_sum_and_mult(fraction_first, fraction_second))