def my_func(arg_1, arg_2, arg_3):
    temp_list = [arg_1, arg_2, arg_3]
    temp_list = sorted(temp_list)[1:]
    k = 0
    for el in temp_list:
        k = k + el
    print(k)


input_list = input('введите 3 числа через пробел: ').split()
input_list = [int(item) for item in input_list]

my_func(input_list[0], input_list[1], input_list[2])