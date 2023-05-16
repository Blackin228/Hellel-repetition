while True:
     name = input('Введите ваше і`мя: ')
     age = input('Введите ваш возраст: ')

     if not age.isdigit() or int(age) <= 0:
        print('Ошибка, повторите ввод')
     elif int(age) < 10:
        print(f'Привет, шкет {name}')
     elif int(age) <= 18:
         print(f'Как жизнь {name}')
     elif int(age) < 100:
         print(f'Что желаете {name}')
     else:
         print(f'{name}, ви лжете - в наше время столько не живут ...')

     if input('Желаете вийти?(Д/Y): ').upper() in ['Y', 'Д']:
         break
