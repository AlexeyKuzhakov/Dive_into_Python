#2. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
#Дано a, b, c - стороны предполагаемого треугольника.
#Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
#Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
#Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def triangle_type(a, b, c):
    if a + b < c or a + c < b or b + c < a:
        return 'Треугольника не существует'
    elif (a + b + c) / 3 == a:
        return 'Треугольник равносторонний'
    elif a == b or a == c or b == c:
        return 'Треугольник равнобедренный'
    else:
        return 'Треугольник разносторонний'

print(triangle_type(9,15,14))