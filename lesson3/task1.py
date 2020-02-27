def my_division(dividend, divider):
    if divider == 0:
        print('Вы пытаетесь поделить на 0, это до хорошего не доводит')
    res = dividend / divider
    print(f'Ответ: {res}')


dividend = float(input('Введите делимое: '))
divider = float(input('Введите делитель: '))
my_division(dividend, divider)
