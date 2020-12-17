def div(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        print('Попытка деления на ноль')
    else:
        return c

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))

print(div(number_1, number_2))