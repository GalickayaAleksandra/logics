# Рассчитать последовательность фибоначчи, длину ряда задает пользовател
element_1 = 0
element_2 = 1
count_element = input('Какое количество элементов вывести на экран? ')
list_fibonachi = [element_1, element_2]
ind = 1
while ind < int(count_element) - 1:
    fn_element = element_1 + element_2
    list_fibonachi.append(fn_element)
    element_1, element_2 = element_2, fn_element
    ind += 1
else:
    print(list_fibonachi)
