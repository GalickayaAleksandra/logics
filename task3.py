# Пользователь вводит значения через запятую, если количество значений меньше 10,
# отсортировать их от большего к меньшему, если больше то от меньшего к большему.
input_values = input('Введите значения через запятую: ')
input_values_clear = input_values.replace('.', ',').replace(' ', ',').replace('/', ',')
pars_values = input_values.split(',')
list_pars_values = [int(i) for i in pars_values if i.isdigit()]
if len(list_pars_values) != 0:
    if len(list_pars_values) < 10:
        print(sorted(list_pars_values))
    else:
        print(sorted(list_pars_values, reverse=True))
else:
    print('Вы ввели буквы вместо цифр')
