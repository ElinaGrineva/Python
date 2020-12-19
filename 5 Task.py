from functools import reduce

my_list = range(100, 1001, 2)


def summa(a, b):
    return a + b


print(reduce(summa, my_list))
