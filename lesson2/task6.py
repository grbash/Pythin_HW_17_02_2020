product_number = 1
finish = input('Введите +, если хотите добавить товар и - если нет: ')
products_list = list()

while finish != '-':
    print(f'Товар номер {product_number}')
    new_product = {
        'название': input('Введите название '),
        'цена': int(input('Введите цену ')),
        'количество': int(input('Введите количество ')),
        'eд': input('Введите единицу измерения ')
    }

    products_list.append((product_number, new_product))
    product_number += 1
    finish = input('Введите +, если хотите продолжить ввод товаров и - если нет: ')
print(products_list)
