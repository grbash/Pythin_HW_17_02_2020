input_list = input("Введи список чисел через пробел: ").split()
input_list = [int(item) for item in input_list]
output_list = []
for i in range(1, len(input_list)):
    if input_list[i] > input_list[i-1]:
        output_list.append(input_list[i])

print(output_list)
