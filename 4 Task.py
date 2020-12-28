translate = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}

with open('translate.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()
    new_content = [f'{translate[line.split(" — ")[0]]} - {line.split(" — ")[-1]}' for line in content]
    print(new_content)

with open('translate_2.txt', 'w', encoding='UTF-8') as f:
    f.writelines(new_content)