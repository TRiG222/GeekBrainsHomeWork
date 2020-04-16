import json

profit = {}
average_profit_dict = {}
my_list = [profit, average_profit_dict]
i = 0
average_profit = 0

with open('text_7.txt', encoding='utf-8') as my_f:
    for line in my_f:
        name, ownership, revenue, costs = line.split()
        profit[name] = int(revenue) - int(costs)
        if profit.setdefault(name) > 0:
            average_profit += profit.setdefault(name)
            i += 1
    if i != 0:
        print(f'Средняя прибыль {i} компаний равна: {average_profit / i}')
    average_profit_dict.update({'Средняя прибыль': (average_profit / i)})
    print(my_list)

with open('my_file.json', 'w', encoding='utf-8') as my_f:
    json.dump(my_list,
              my_f,
              ensure_ascii=False,
              indent=4)
