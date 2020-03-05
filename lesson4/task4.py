from random import randint

my_list = [randint(-15, 15) for i in range(40)]
output_list = [el for el in my_list if my_list.count(el) == 1]
# изначально написал с .append , но в разборе задания 2 увидел более удобный и емкий способ формирования списка
# и переписал с ним

print(my_list)
print(output_list)