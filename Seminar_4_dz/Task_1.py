# Напишите функцию для транспонирования матрицы

matrix = [[1, 2, 3],
          [10, 20, 30],
          [100, 200, 300]]

print("Исходная матрица:\n", matrix)

def matrix_transposition(matrix):
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    print(trans_matrix)


print("Транспонированная матрица:")
matrix_transposition(matrix)