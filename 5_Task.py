revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))

if revenue > costs:
    profitability = revenue / costs
    print(f'Ура. У фирмы прибыль. Рентабельность составила: {profitability:.2f}')
    num_of_employ = int(input('Введите кол-во сотрудников фирмы: '))
    profit_per_1_employ = (revenue - costs) / num_of_employ
    print(f'Прибыль фирмы в расчете на одного сотрудника составила: {profit_per_1_employ:.2f}')

else:
    print('У фирмы убыток')
