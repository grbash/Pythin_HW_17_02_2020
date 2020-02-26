month_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
seasons = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn', 'autumn', 'autumn',
           'winter']
seasons_dict = dict(zip(month_number, seasons))

input_number = int(input('Enter number from 1 to 12: '))
print(f'List output: {seasons[input_number - 1]}')
print(f'Dict output: {seasons_dict.get(input_number)}')
