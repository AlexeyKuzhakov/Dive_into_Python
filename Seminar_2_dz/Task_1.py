# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input('Введите целое число: '))

# Преобразование через функцию:
def to_hex(num):
    number = num
    hex_digits = '0123456789abcdef'
    hex_str = ''
    while num > 0:
        hex_str = (hex_digits[num % 16] + hex_str)
        num //= 16
    return f'Число {number} в шестнадцатиричном представлении = 0x' + hex_str

print(to_hex(num))

# С использованием метода format
print(format(num, '#x'))

# Проверка hex
print(hex(num))