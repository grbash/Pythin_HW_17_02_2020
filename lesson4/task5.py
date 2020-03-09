from functools import reduce


def multi_list(el_1, el_2):
    return el_1 * el_2


my_list = [i for i in range(100, 1001, 2)]
output = reduce(multi_list, my_list)
print(my_list)
print(output)

# как Python хранит и выводит такие огромные числа? если я ничего не пропустил, вы не рассказывали об этом
