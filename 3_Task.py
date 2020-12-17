def my_func(a,b,c):
    l = [a,b,c]
    l.sort(reverse=True)
    sum = l[0]+l[1]
    return sum

result = my_func(6,4,2)

print(f'Сумма наибольших двух аргументов равна: {result}')