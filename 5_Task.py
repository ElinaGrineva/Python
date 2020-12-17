while True:
    numbers = input('Введите строку чисел через пробел. Для выхода нажмите Q: ').split()

    if numbers == ['Q']:
        break
    else:
        numbers = list(map(int, numbers))
        print(sum(numbers))
#  Подскажите, пожалуйста, как сделать так, чтобы сумма вновь введеных чисел была добавлена к уже подсчитанной сумме.