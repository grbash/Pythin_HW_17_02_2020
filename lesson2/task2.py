my_list = input('Input list items: ').split()
i = 0

for el in my_list:
    if i != len(my_list) - 1:
        if i % 2 == 0:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 1

print(my_list)
