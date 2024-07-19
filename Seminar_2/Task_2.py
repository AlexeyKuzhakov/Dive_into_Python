
data = [42, 73.0, 'Hello world!', True, 42, 'Hello world!', 256, 2 ** 8, 1, 'Привет мир!']

for i, item in enumerate(data, start=1):
    print(f'{i} значение {item}, адрекс {id(item)}, размер {item.__sizeof__()}, хэш {hash(item)}')
    if isinstance(item, int):
        print('Это целове число')
    elif isinstance(item, str):
        print('Это строка')
    print()