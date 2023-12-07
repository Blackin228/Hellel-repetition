def progression(value, den):
    while True:
        value *= den
        yield value


value = int(input('Введіть перше значення прогресії: '))
den = int(input('Введіть знаменник прогресії: '))
count = int(input('Введіть кількість значень, які ви хочете побачити: '))

for index, item in enumerate(progression(value, den)):
    if index == count:
        break
    print(item)
