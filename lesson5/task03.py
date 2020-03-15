with open("task03_text.txt", "r") as input_file:
    salaries = []
    salaries_less_20000 = []
    for el in input_file:
        el = el.split()
        if float(el[1]) < 20000:
            salaries_less_20000.append(el[0])
        salaries.append(el[1])

avg_salary = sum(map(float, salaries)) / len(salaries)
print(f"Зарплаты менее 20тыс. у {salaries_less_20000}. \nСредняя зарплата: {avg_salary}")
