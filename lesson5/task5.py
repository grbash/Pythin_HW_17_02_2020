from random import randint

output_sum = 0
with open("task5_text.txt", "w") as output_file:
    for i in range(randint(10, 100)):
        item = randint(1, 200)
        output_sum = output_sum + item
        output_file.write(str(item) + " ")

print(f"Сумма всех элементов: {output_sum}")
