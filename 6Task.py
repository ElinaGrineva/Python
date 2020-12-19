from itertools import count, cycle
from sys import argv

script_name, number, repeat = argv
print(argv)

for el in count(int(number)):
    if el == 11:
        break
    print(el)

count = 0
for el in cycle(repeat):
    if count > 7:
        break
    print(el)
    count += 1

