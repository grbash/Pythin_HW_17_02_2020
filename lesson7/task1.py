class Matrix:
    def __init__(self, input_list):
        self.list = input_list

    def __str__(self):
        return str("\n".join(["\t".join([str(i) for i in j]) for j in self.list]))

    def __add__(self, other):
        res = []
        for i in range(len(self.list)):
            res.append([])
            for j in range(len(self.list[i])):
                res[i].append(self.list[i][j] + other.list[i][j])
        return str("\n".join(["\t".join([str(i) for i in j]) for j in res]))


a = []
b = []
number_of_strings = int(input("Введите количесвто строк в матрицах: "))
number_of_rows = int(input("Введите количесвто столбцов в матрицах: "))

print("Введите значения первой матрицы: ")
for i in range(number_of_strings):
    a.append([])
    print(f"Введите значения {i + 1} строки попарядку слева направо: ")
    for j in range(number_of_rows):
        a[i].append(int(input(f"Значение {j + 1}: ")))
matrix_1 = Matrix(a)
print(f"Матрица 1: \n{matrix_1} \n ")

print("Введите значения второй матрицы: ")
for i in range(number_of_strings):
    b.append([])
    print(f"Введите значения {i + 1} строки попарядку слева направо: ")
    for j in range(number_of_rows):
        b[i].append(int(input(f"Значение {j + 1}: ")))
matrix_2 = Matrix(b)
print(f"Матрица 2 \n{matrix_2} \n ")
print(f"Вы ввели матрицы: \n{matrix_1}\n\n{matrix_2}")
print(f"Сумма матриц \n{matrix_1 + matrix_2}")
