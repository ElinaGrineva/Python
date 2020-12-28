import json

with open('firm.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()
    average_profit = 0
    res = {}

    for i in content:
        name, form, revenue, costs = i.split()
        revenue = float(revenue)
        costs = float(costs)
        profit = revenue - costs
        res[name] = profit
        if profit >= 0:
            average_profit += profit

res['average_profit'] = round (average_profit / len(content), 2)

with open('firm.json', 'w', encoding='UTF-8') as file:
    json.dump(res, file)