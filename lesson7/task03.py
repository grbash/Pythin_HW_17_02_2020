class Cell:
    def __init__(self, input_number):
        self.number_of_cells = input_number

    def make_order(self, number_of_rows):
        return "\n".join(["*" * number_of_rows for i in range(self.number_of_cells // number_of_rows)]) + "\n" + "*" * (
                self.number_of_cells % number_of_rows)

    def __str__(self):
        return self.number_of_cells

    def __add__(self, other):
        return f"Сумма клеток: {self.number_of_cells + other.number_of_cells}"

    def __sub__(self, other):
        if self.number_of_cells - other.number_of_cells > 0:
            return self.number_of_cells - other.number_of_cells
        else:
            return "Вычитание невозможно, клеток в первой ячейке должно быть строго больше клеток во второй ячейке"

    def __mul__(self, other):
        return f"Произведение клеток: {self.number_of_cells * other.number_of_cells}"

    def __truediv__(self, other):
        if other.number_of_cells == 0:
            return "Во второй ячейке количество клеток должно быть больше 0"
        else:
            return f"Деление клеток: {round(self.number_of_cells / other.number_of_cells)}"


num_of_cells_in_1 = int(input("Введите количетсво клеток в первой ячейке: "))
num_of_cells_in_2 = int(input("Введите количетсво клеток в второй ячейке: "))
rows_in_cell = int(input("Введите количетсво ячеек в ряду: "))

cell_1 = Cell(num_of_cells_in_1)
cell_2 = Cell(num_of_cells_in_2)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(rows_in_cell))
print(cell_2.make_order(rows_in_cell))
