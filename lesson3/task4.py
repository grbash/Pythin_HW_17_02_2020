# вспомнил такой способ возведения числа в степень первым.
def exp(x, n):
    if n == 0:
        return 1
    return x * exp(x, n - 1)


def my_func(x, y):
    print(f' С использованием ** {x ** y}')

    print(f'Без использования ** {1 / exp(x, -y)}')


x = float(input('Input x: '))
y = int(input('Input y: '))
my_func(x, y)
