number = input('Введите целое положительное число: ')
print(max(str(number)))

# or (Этот способ мне особо не понятен)

number = int(input('Введите целое положительное число: '))

maximum = number%10
number = number//10

while number > 0:
    if number%10 > maximum:
        maximum = number%10
    number = number//10
print(maximum)


