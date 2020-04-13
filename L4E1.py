from sys import argv

try:
    script_name, hour, rate, prize = argv
    hour = int(hour)
    rate = int(rate)
    prize = int(prize)

    if rate and hour > 0:
        print("Имя скрипта: ", script_name)
        print("Рассчет зп: ", hour * rate + prize)
    else:
        print('Чтобы посчитать зп значения должны быть больше нуля')

except ValueError:
    print('Значений должны быть 3 и в числовом формате!')
