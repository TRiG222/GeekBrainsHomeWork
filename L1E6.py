first_day = input('Введите значение a ')
first_day = int(first_day)
end_km = input('Введите значение b ')
end_km = int(end_km)

day = 2

while int(end_km) >= first_day:
    result_day = first_day + (first_day / 100 * 10)
    first_day = result_day
    if first_day >= end_km:
        print(f'На {day} день спортсмен добъется результата - не менее {end_km}км')
    else:
        day += 1
