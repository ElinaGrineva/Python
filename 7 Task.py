from math import factorial

def fact(n):
    for el in range(1, n + 1):
        yield el

for el in fact(n=4):
    print(el)

print(factorial(4))

