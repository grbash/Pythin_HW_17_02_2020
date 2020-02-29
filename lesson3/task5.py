def my_func(prev_sum, my_list):
    temp_sum = 0
    for el in my_list:
        temp_sum = temp_sum + el
    return prev_sum + temp_sum


trigger = 0
fin_sum = 0
while True:
    input_list = input('Введите числа через пробел (стоп символ "+"): ').split()
    for el in input_list:
        if el == '+':
            input_list = input_list[:input_list.index(el)]
            input_list = [int(item) for item in input_list]
            fin_sum = my_func(fin_sum, input_list)
            print(f'Финальная сумма - {fin_sum}')
            trigger = 1
    if trigger == 0:
        input_list = [int(item) for item in input_list]
        fin_sum = my_func(fin_sum, input_list)
        print(f'Текущая сумма - {fin_sum}')
    else:
        break
