month = int(input('Введите месяц в цифровом формате: '))

months = {'зима': [12, 1, 2,], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}

for k, v in months.items():
    if month in v:
        print(k)

