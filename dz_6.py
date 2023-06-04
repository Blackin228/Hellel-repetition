from random import randint as rand

def check_num(number):
    if number.isdigit():
        return True
    elif number.isalpha():
        print('Enter number, not letter')
        return False
    elif not number.isalnum():
        print('Enter number, not symbol')
        return False


def input_nums():
    while True:
        low_num = input('Please enter the lower limit: ')
        if check_num(low_num):
            break
    while True:
        high_num = input('Please enter the higher limit: ')
        if check_num(high_num):
            break
    return rand(int(low_num), int(high_num))


def user_num():
    while True:
        u_num = input('Please enter your number: ')
        if check_num(u_num):
            break
    return int(u_num)



def equality_check():
    random_num = input_nums()
    print(random_num)
    while True:
        u_num = user_num()
        print(u_num)
        if u_num == random_num:
            print('Congratulations, you guessed it')
            break
        elif u_num < random_num:
            print('Your number is lower')
        elif u_num > random_num:
            print('Your number is higher')

equality_check()
