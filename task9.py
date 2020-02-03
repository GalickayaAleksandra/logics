# Пользователь вводит целое число, определить простое ли оно
some_number = input('Ввелите число: ')
float_number = some_number.split(',')
if len(float_number) == 2:
    if float_number[0].isdigit() and float_number[1].isdigit():
        print('Простыми числами могут быть только целые числа')
    else:
        print('Введена строка')
elif len(float_number) == 1:
    if some_number.isdigit():
        some_number = int(some_number)
        sqrt_number = int(some_number ** (1 / 2))
        cnt = 0
        for i in range(2, sqrt_number + 1):
            if (some_number % i) == 0:
                cnt += 1
        if cnt > 0:
            print('Составное число')
        else:
            print('Простое число')
    else:
        print('Введена строка')
else:
    print('Введена строка')
