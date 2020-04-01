revenues = input('Введите значение выручки: ')
cost = input('Введите значение издержки: ')
profit = int(revenues)-int(cost)

if revenues > cost:
    print(f'Ваша прибыль = {profit}')
    profitability = profit / int(revenues)
    print(f'Рентабельность равна {profitability}')
    workers = input('Введите численность сотрудников: ')
    profit_workers = profit / int(workers)
    print(f'Прибыль фирмы в расчете на одного сотрудника{profit_workers}')
elif revenues == cost:
    print('Вы отработали в ноль')
else:
    print(f'Ваш убыток = {profit:}')


