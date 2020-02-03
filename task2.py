# Пользователь вводит число, если оно четное вывесть - “Even” если нет - “Odd”
number = input('Number: ')
cnt_number = number.split('.')
if len(cnt_number) < 2:
    if number.isdigit():
        if int(number) % 2 == 0:
            print('Even')
        else:
            print('Odd')
    else:
        print('Введена строка')
else:
    print('Вы ввели вещественное число')
