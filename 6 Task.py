with open('subjects.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()
    res = {}

    for i in content:
        subject, number1, lection, number2, practical, number3, laboratory = i.split()
        numbers = float(number1) + float(number2) + float(number3)
        res[subject] = numbers
print(res)