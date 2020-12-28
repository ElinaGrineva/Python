with open('numbers.txt', 'w', encoding='UTF-8') as file:
    numbers = input('Введите любые числа через пробел: ')
    file.write(numbers)

with open('numbers.txt', 'r', encoding='UTF-8') as f:
    content = f.read()
    print(sum([int(number) for number in content.split()]))
