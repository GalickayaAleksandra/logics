# Дан список из целых чисел длиной N подсчитать количество четных чисел в списке
some_list = [2, 4, 1, 5, 7, 10, 16]
count_number = 0
for i in some_list:
    if i % 2 == 0:
        count_number += 1
print(count_number)