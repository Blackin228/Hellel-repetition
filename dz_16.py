import json

input_dict = {
    111111: ('Jon', 15),
    222222: ('Sam', 22),
    333333: ('Tom', 19),
    444444: ('Nick', 26),
    555555: ('Tim', 13),
    667667: ('John', 36)
}

with open('dz_16.json', 'w') as file:
    json.dump(input_dict, file)

with open('dz_16.json') as file:
    data = json.load(file)

print(data)
print(type(data))
