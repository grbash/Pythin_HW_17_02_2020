my_list = input('Input something: ').split()

for el in my_list:
    if len(el) >= 10:
        print(el[:10])
    else:
        print(el)