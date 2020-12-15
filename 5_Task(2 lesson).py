my_list = [7, 5, 3, 3, 2]

number = int(input('Введите число в рейтинге: '))

while len(my_list) != 10:
    my_list.append(number)
    my_list.sort(reverse=True)
    print(my_list)
    number = int(input('Введите число в рейтинге: '))

