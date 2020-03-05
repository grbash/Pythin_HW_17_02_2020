from itertools import count, cycle

print('а) генерация целый чисел, начиная с выбранного пользователем, для продолжения нажмите Enter, для заверщения +')

for i in count(int(input('Вевдите стартовое число: '))):
    print(i, end='')
    finish = input()
    if finish == '+':
        break

print('b) перебор заранее заданного списка, для продолжения нажмите Enter, для заверщения +')
# изначально эту часть программы реализовал, как в методичке, но после просмотра разбора доработал в соответствии
# с первым способ решения
my_list = input('Введите список, елементы которого будем перебирать, через пробел: ').split()
temp_item = cycle(my_list)
finish = ''

while finish != '+':
    print(next(temp_item), end='')
    finish = input()

