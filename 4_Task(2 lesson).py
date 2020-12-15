string = input('Введите строку из нескольких слов, разделенных пробелами')
strings = string.split()

for i, el in enumerate(strings):
    print(i, el)
