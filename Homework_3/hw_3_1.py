'''Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X.'''

<<<<<<< HEAD
n = int(input("Введите количество элементов: "))
#list_1 = [1,2,3,3,5,3,2,2,2,2,2]
list_1 = [int(input()) for i in range(n)]
print (list_1)
count = 0
x = int(input("Введите искомый элемент: "))
for i in range(len(list_1)):
    if list_1[i] == x:
            count += 1
print (count)
=======
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

>>>>>>> 3_homework
