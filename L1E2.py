time_s = input('Введите время в секундах: ')
time_h = (int(time_s) // 3600)
time_m = (int(time_s) // 60)

hours, minutes, seconds = time_h, time_m, time_s

print(f'{hours:02}:{minutes:02}:{seconds}')
