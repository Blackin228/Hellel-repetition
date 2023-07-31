values = [1, 2, '3', 'forth', 'end', 99, True, None]
print(f'Start list of values: {values}')
new_values = list(map(lambda x: str(x) if type(x) == int else x, values))
print(f'Output list of values: {new_values}')
