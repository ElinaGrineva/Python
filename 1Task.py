from sys import argv

script_name, hour, rate, bonus = argv


def payroll(a, b, c):
    d = (a * b) + c
    return d


print(f'Заработная плата сотрудника составит: ', payroll(int(argv[1]), int(argv[2]), int(argv[3])))

