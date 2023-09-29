def check_for_exit(x):
     return x.lower() in ('exit', 'quit', 'e', 'q')


def check_for_clear_input(x):
    if x[0:2] == '-.':
        return x[2::].isnumeric()
    elif x[0] == '-':
        if x.count('.') == 1:
            return x[1::].replace('.', '').isdigit()
        return x[1::].isdigit()
    elif x[0] == '.':
        return x[1::].isdigit()
    elif x.count('.') == 1:
        return x.replace('.', '').isdigit()
    else:
        return x.isdigit()


def check_number(number):
    if float(number) == 0:
        return 'zero'
    message = ''
    if number[0] == '-':
        message += 'negative'
    else:
        message += 'positive'
    message += ' '
    if '.' in number:
        message += 'fractional'
    else:
        message += 'integer'
    return message


def main():
    while True:
        print('''Please enter any number if you want to check which number it is.
If you want to close the program, Please write "quit", "exit", "q" or "e"''')
        answer = input()

        if check_for_exit(answer):
            break
        input_value = answer.replace(',', '.')

        if check_for_clear_input(input_value):
            print(f'You entered {check_number(input_value)} number: '
                  f'{"-0."+input_value[2::] if input_value[0:2] == "-." else input_value}')
        else:
            print(f'You entered incorrect value: {input_value}. Please enter correct value.')
        print('*' * 70)

main()
