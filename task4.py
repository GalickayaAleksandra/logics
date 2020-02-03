# Пользователь вводит 2 числа, если первое больше второго, вывести их разность,
# если второе больше первого вывести их сумму, если числа равны, возвести первое в степень второго.
first_number = input('First number: ')
second_number = input('Second number: ')
first_number_values = first_number.split('.')
second_number_values = second_number.split('.')
if len(first_number_values) < 2:
    if len(second_number_values) < 2:
        if first_number.isdigit() and second_number.isdigit():
            first_number = int(first_number)
            second_number = int(second_number)
            if first_number > second_number:
                print(first_number - second_number)
            elif second_number > first_number:
                print(first_number + second_number)
            else:
                print(first_number ** second_number)
        else:
            print("Введена строка")
    elif len(second_number_values) == 2:
        if first_number.isdigit() and second_number_values[0].isdigit() and second_number_values[1].isdigit():
            first_number = float(first_number)
            second_number = float(second_number)
            if first_number > second_number:
                print(first_number - second_number)
            elif second_number > first_number:
                print(first_number + second_number)
            else:
                print(first_number ** second_number)
elif len(first_number_values) == 2:
    if len(second_number_values) < 2:
        if first_number_values[0].isdigit() and first_number_values[1].isdigit() and second_number.isdigit():
            first_number = float(first_number)
            second_number = float(second_number)
            if first_number > second_number:
                print(first_number - second_number)
            elif second_number > first_number:
                print(second_number + first_number)
            else:
                print(first_number ** second_number)
        print('Введена строка')

    elif len(second_number_values) == 2:
        if first_number_values[0].isdigit() and first_number_values[1].isdigit() and second_number_values[0].isdigit() \
                and second_number_values[1].isdigit():
            first_number = float(first_number)
            second_number = float(second_number)
            if first_number > second_number:
                print(first_number - second_number)
            elif second_number > first_number:
                print(second_number + first_number)
            else:
                print(first_number ** second_number)
        else:
            print('Введена строка')
else:
    print('Вы ввели строку')
