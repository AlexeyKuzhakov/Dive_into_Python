
from random import uniform

a = uniform(-100, 100)
b = uniform(-100, 100)
c = uniform(-100, 100)

print(f'{a}x^2 + {b}x + {c} = 0')
d = b ** 2 - 4 * a * c
print(f'{d=}')
if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    result = f'Уровнение имеет два корня: {x1= }, {x2= }'
elif d == 0:
    x = -b / (2 * a)
    result = f'Уровнение имеет один корень: {x= }'
else:
    d = complex(d, 0)
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    result = f'Уровнение имеет два комплексных корня: {x1= }, {x2= }'

print(result)