from itertools import count
from math import factorial


def my_func():
    for i in count(1):
        yield factorial(i)


finish = int(input('Введи число, до которого надо считать факториал: '))
x = 0
for i in my_func():
    if x <= finish - 1:
        x = x + 1
        print(f'Fact {x} = {i}')
    else:
        break
