class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                y_or_n = input(f'Хотите попробоващь еще? Введите да или нет: ')

                if y_or_n == 'да':
                    print(try_except.my_input())
                elif y_or_n == 'нет':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'


try_except = Error(1)
print(try_except.my_input())
