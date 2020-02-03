# Пользователь вводит 3 числа, подставить и посчитать формулу: 2a - 8b / (a-b+c). Вывести результат.
number_first = input("Введите a: ")
number_second = input("Введите b: ")
number_three = input("Введите c: ")
point_number_first = number_first.find(".")
point_number_second = number_second.find(".")
point_number_three = number_three.find(".")
if point_number_first == -1 and point_number_second == -1 and point_number_three == -1:
    if number_first.isdigit() and number_second.isdigit() and number_three.isdigit():
        number_first = int(number_first)
        number_second = int(number_second)
        number_three = int(number_three)
        result = 2 * number_first - 8 * number_second / (number_first - number_second + number_three)
        print(result)
    else:
        print("Введена строка")
elif point_number_first != -1 and point_number_second == -1 and point_number_three == -1:
    split_number_first = number_first.split(".")
    if split_number_first[0].isdigit() and split_number_first[1].isdigit() and number_second.isdigit()\
            and number_three.isdigit():
        number_first = float(number_first)
        number_second = float(number_second)
        number_three = float(number_three)
        result = 2 * number_first - 8 * number_second / (number_first - number_second + number_three)
        print(result)
    else:
        print("Введена строка")
elif point_number_first == -1 and point_number_second != -1 and point_number_three == -1:
    split_number_second = number_second.split(".")
    if split_number_second[0].isdigit() and split_number_second[1].isdigit() and number_first.isdigit() \
            and number_three.isdigit():
        number_first = float(number_first)
        number_second = float(number_second)
        number_three = float(number_three)
        result = 2 * number_first - 8 * number_second / (number_first - number_second + number_three)
        print(result)
    else:
        print("Введена строка")
elif point_number_first == -1 and point_number_second == -1 and point_number_three != -1:
    split_number_three = number_three.split(".")
    if split_number_three[0].isdigit() and split_number_three[1].isdigit() and number_first.isdigit() \
            and number_second.isdigit():
        number_first = float(number_first)
        number_second = float(number_second)
        number_three = float(number_three)
        result = 2 * number_first - 8 * number_second / (number_first - number_second + number_three)
        print(result)
    else:
        print("Введена строка")
elif point_number_first != -1 and point_number_second != -1 and point_number_three == -1:
    split_number_first = number_first.split(".")
    split_number_second = number_second.split(".")
    if split_number_first[0].isdigit() and split_number_first[1].isdigit() and split_number_second[0].isdigit() \
                                       and split_number_second[1].isdigit() and number_three.isdigit():
        number_first = float(number_first)
        number_second = float(number_second)
        number_three = float(number_three)
        result = 2 * number_first - 8 * number_second / (number_first - number_second + number_three)
        print(result)
    else:
        print("Введена строка")
elif point_number_first != -1 and point_number_second == -1 and point_number_three != -1:
    split_number_first = number_first.split(".")
    split_number_three = number_three.split(".")
    if split_number_first[0].isdigit() and split_number_first[1].isdigit() and split_number_three[0].isdigit() \
                                       and split_number_three[1].isdigit() and number_second.isdigit():
        number_first = float(number_first)
        number_second = float(number_second)
        number_three = float(number_three)
        result = 2 * number_first - 8 * number_second / (number_first - number_second + number_three)
        print(result)
    else:
        print("Введена строка")
elif point_number_first == -1 and point_number_second != -1 and point_number_three != -1:
    split_number_second = number_second.split(".")
    split_number_three = number_three.split(".")
    if split_number_second[0].isdigit() and split_number_second[1].isdigit() and split_number_three[0].isdigit() \
                                        and split_number_three[1].isdigit() and number_first.isdigit():
        number_first = float(number_first)
        number_second = float(number_second)
        number_three = float(number_three)
        result = 2 * number_first - 8 * number_second / (number_first - number_second + number_three)
        print(result)
    else:
        print("Введена строка")
elif point_number_first != -1 and point_number_second != -1 and point_number_three != -1:
    split_number_first = number_first.split(".")
    split_number_second = number_second.split(".")
    split_number_three = number_three.split(".")
    if split_number_first[0].isdigit() and split_number_first[1].isdigit() and split_number_second[0].isdigit() \
                                       and split_number_second[1].isdigit() and split_number_three[0].isdigit()\
                                       and split_number_three[1].isdigit():
        number_first = float(number_first)
        number_second = float(number_second)
        number_three = float(number_three)
        result = 2 * number_first - 8 * number_second / (number_first - number_second + number_three)
        print(result)
else:
    print("Введена строка")