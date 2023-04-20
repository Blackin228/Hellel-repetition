import copy

input_str = input('Please enter any string: ')
print('I`ts string, where letters is even: ' ,input_str[1::2])
print('It`s string, where the capital letters are in reverse order: ', input_str[-1::-1].upper())

var_1 = 50
var_2 = 50
var_3 = 50
print('Three variables')
print('*' * 50)
print('var_1 = ', var_1)
print('var_2 = ', var_2)
print('var_3 = ', var_3)
print('Check: ')
print('var_1 == var_2 == var_3: ', var_1 == var_2 == var_3)
print('var_1 is var_2 is var_3: ', var_1 is var_2 is var_3)
print("Checking changed variables:")
print('var_1 == var_2 == var_3: ', float(var_1) == float(var_2) == float(var_3))
print('var_1 is var_2 is var_3: ', float(var_1) is float(var_2) is float(var_3))
print('*' * 50, end= '\n\n\n')

var_1 = [50, 'a']
var_2 = [50, 'a']
print('Two variables')
print('*' * 50)
print('var_1 = ', var_1)
print('var_2 = ', var_2)
print('Check: ')
print('var_1 == var_2: ', var_1 == var_2)
print('var_1 is var_2: ', var_1 is var_2)
print("Checking changed variables:")
print('var_1 == var_2: ', bool(var_1) == bool(var_2))
print('var_1 is var_2: ', bool(var_1) is bool(var_2))

