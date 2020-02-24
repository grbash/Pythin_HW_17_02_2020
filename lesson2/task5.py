input_number = int(input('Input number: '))
my_list = [7, 5, 3, 3, 2]
i = 0

while i < len(my_list) and my_list[i] >= input_number:
    i += 1
my_list.insert(i, input_number)

print(my_list)
