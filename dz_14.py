data = b'r\xc3\xa9sum\xc3\xa9'

print(f'String in byte form: {data}')
print(f'String in standard decoded form: {data.decode()}')
data_latin1 = data.decode().encode('Latin1')
print(f'String in byte form by Latin1: {data_latin1}')
print(f'String in standard form: {data_latin1.decode("Latin1")}')
