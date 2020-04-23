class Matrix:
    def __init__(self, m_1):  # конструктор
        self.m_1 = m_1

    def __str__(self):  # вывод матрицы в привычном виде
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.result]))

    def __add__(self, other):  # сложение матриц
        self.result = [[0, 0],
                       [0, 0],
                       [0, 0]]

        for i in range(len(self.m_1)):

            for j in range(len(self.m_1[i])):
                self.result[i][j] = self.m_1[i][j] + self.m_1[i][j]
        return self.result


matrix_1 = Matrix([[1, 2], [2, 3], [3, 4]])

matrix_2 = Matrix([[1, 2], [2, 3], [3, 5]])

matrix_1 + matrix_2
print(matrix_1)

