'''не понял по поводу использования list и dict
нужно было чтоб они взаимодейтсвовали между собой
или вывод оттуда и оттуда'''

season_list = ['winter', 'spring', 'summer', 'autumn']
season_dict = {1: season_list[0],
               2: season_list[1],
               3: season_list[2],
               4: season_list[3]}

month = int(input('Введите номер месяца: '))
if month == 1 or month == 2 or month == 12:
    print(season_dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print(season_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(season_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(season_dict.get(4))
else:
    print('Не верное значение!')
