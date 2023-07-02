'''Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X.'''

from random import randint as rd
N = int(input("Введите количество элементов: "))
min = int(input("Введите минимальное значение для заполнения списка: "))
max = int(input("Введите максимальное значение для заполнения списка: "))

numbers = list()
for i in range (N):
    numbers.append(rd(min, max))
print (numbers)

count = 0
x = int(input("Введите искомый элемент: "))
for i in range(len(numbers)):
    if numbers[i] == x:
            count += 1
print (count)

