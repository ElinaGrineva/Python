with open('employees.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()
    person_with_low_salary = []
    average_salary = 0

    for i in content:
        surname, salary = i.split()
        salary = float(salary)
        average_salary += salary
        if salary < 20000:
            person_with_low_salary.append(surname)

    print(f'ЗП меньше 20000 тыс.: {person_with_low_salary}')
    print(f'Средний доход: {average_salary / len(content)}')



