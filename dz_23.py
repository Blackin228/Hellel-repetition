class RaisingToTheZeroPower(Exception):
    def __init__(self, message='Ви хочете піднести число в нульову степінь'):
        super().__init__(message)


class Calculator(object):

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

    @staticmethod
    def div(x, y):
        try:
            return x/y
        except ZeroDivisionError:
            return 'На нуль ділити не можна'

    @staticmethod
    def mul(x, y):
        return x*y

    @staticmethod
    def pow(x, y):
        try:
            if y == 0:
                raise RaisingToTheZeroPower
            else:
                return x**y
        except RaisingToTheZeroPower as err:
            return err

    @staticmethod
    def sqrt(x, y):
        return x**(1/y)


def main():
    choices = {'1': Calculator.add, '2': Calculator.sub, '3': Calculator.div, '4': Calculator.mul, '5': Calculator.pow,
               '6': Calculator.sqrt}
    while True:
        print('''Ця програма примітивний калькулятор
        Введіть число, яке відповідає дії, яку ви хочете виконати над двома числами: 
        1 -> додати
        2 -> відняти
        3 -> поділити
        4 -> помножити
        5 -> піднесення до степені
        6 -> вилучення корення
        7 -> вийти''')
        choice = input(' ')
        if choice == '7':
            break
        print('Введіть два числа')
        while True:
            num_1 = input('Перше число: ')
            num_2 = input('Друге число: ')
            if num_1.isdigit() or num_2.isdigit():
                break
            else:
                print('Ви ввели не число. Введіть, будь ласка числа.')
        print(choices[choice](int(num_1), int(num_2)))
        print('-'*50)


main()
