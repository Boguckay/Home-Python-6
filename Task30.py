'''Задача 30: Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.'''


'''a1 = int(input())
d = int(input())
n = int(input())
for i in range(n):
    print(a1 + i * d)'''

from Module_for_HW_6 import arithmetic_sequence

a1 = int(input('Введите первый член последовательности: '))
a_diff = int(input('Введите разность между членами последовательности: '))
n = int(input('Введите количество членов последовательности: '))
print(*arithmetic_sequence(a1, a_diff, n))