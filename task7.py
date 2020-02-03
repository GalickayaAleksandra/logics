# Дан список целых чисел длиной N отсортировать список, не используя метода sort или sorted.
some_list = [2, 6, 3, 1, 7]
sort_list = []
ind = 0
while ind <= len(some_list) - 1:
    sort_list = some_list[ind:len(some_list)]
    min_element = min(sort_list)
    ind_min_element = sort_list.index(min_element)
    sort_list[0], sort_list[ind_min_element] = sort_list[ind_min_element], sort_list[0]
    some_list[ind:len(some_list)] = sort_list
    ind += 1
else:
    print(some_list)
