
DIV_BIN = 2
DIV_OCT = 8
original_num: int = int(input('Введите целое цисло: '))

for div in (DIV_BIN, DIV_OCT):
    num = original_num
    result: str = ''
    while num > 0:
        result = str(num % div) + result
        num //= div
    print(f'Число {original_num} в {div} системе: {result}')