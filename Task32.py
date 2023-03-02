'''Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не меньше
заданного минимума и не больше заданного максимума)'''


from Module_for_HW_6 import create_list, indexes_of_numbers

num_list = create_list(int(input('Введите размер массива: ')))
left_endpoint = int(input('Введите минимум диапазона: '))
right_endpoint = int(input('Введите максимум диапазона: '))

print(*num_list)
print(*indexes_of_numbers(num_list, left_endpoint, right_endpoint))


'''list_1 = [-5, 9, 0, 3, -1, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5,-5, 7]
min_number = int(input())
max_number = int(input())
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i)''
