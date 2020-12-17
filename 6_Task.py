def int_func(a):
    b = a.title()
    return b

print(int_func('text me today'))

# Если пользовать вводит с маленькой буквы, то можно приобразовать результат сразу вот так:

text = input('Введите слово: ').title()
print(text)