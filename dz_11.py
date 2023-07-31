input_data =  ['Страна', 'шалашє', 'Летел', 'вертолет', 'УЧУ', 'мєм', 'язик']
print(f'Start list of values: {input_data}')
output_data = list(filter(lambda x: x.lower() == x.lower()[::-1], input_data))
print(f'Output list of values: {output_data}')
