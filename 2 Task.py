with open('text.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()
    print(f'Кол-во строк: {len(content)}')
    for i, el in enumerate(content):
        print(f'Количество слов в строке {i+1}: {len(el.split())}')





