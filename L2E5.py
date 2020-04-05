my_list = [1, 4, 6, 7, 3, 2]

list_position = 0

new_rate = int(input('Введите новый элемент рейтинга: '))
for i in my_list:
    list_position += 1
    if i == new_rate:
        my_list.insert(list_position, new_rate)
        print(my_list)
        break
    elif my_list.count(new_rate) == 0:
        my_list.append(new_rate)
        print(my_list)
        break


