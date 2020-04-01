number = input('Введите целое положительное число: ')
number = int(number)
max_number = 1

while number > 10:
    i = number % 10
    if i == 9:
        max_number = i
        break
    number = number // 10
    if i > max_number:
        max_number = i
print(max_number)



