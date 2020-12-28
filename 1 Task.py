with open('my_file.txt', 'w', encoding='UTF-8') as file:
    while True:
        text = input('Введите текст: ')
        if text == '':
            break
        file.write(f'{text}\n')

