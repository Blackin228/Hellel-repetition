string_1 = input('Please enter first string: ')
string_2 = input('Please enter second string: ')
string_3 = input('Please enter third string: ')
string_4 = input('Please enter fourth string: ')
with open('dz_15.txt', 'w') as f:
    f.write(string_1 + '\n' + string_2 + '\n')

with open('dz_15.txt', 'a') as f:
    f.write(string_3 + '\n' + string_4 + '\n')
