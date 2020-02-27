def my_func(name, second_name, year_of_birth, city, email, tel):
    print(
        f'Вас зовут - {name}, Ваша фамилия - {second_name}, Ваш год рождения - {year_of_birth}, Ваш город - {city}, '
        f'Ваш email - {email}, Ваш номер телефона - {tel}'
    )


name = input('Ведите имя: ')
second_name = input('Ведите фамилию: ')
year = int(input('Ведите год рождения: '))
city = input('Ведите город: ')
email = input('Ведите email: ')
tel_num = input('Ведите номер телефона: ')
my_func(name=name, second_name=second_name, year_of_birth=year, city=city, email=email, tel=tel_num)
