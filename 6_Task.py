a = int(input('Введите результат бега первого дня в км: '))
b = int(input('Введите желаемый результат бега в км: '))

day = 1
result_km = a
print('Результат:')
print(f'1-й день: {a}')

while result_km < b:
    a = a + 0.1 * a
    day += 1
    result_km = a
    print(f'{day}-й день: {result_km:.2f}')

print(f'Вы достигнете требуемых показателей на {day} день')





