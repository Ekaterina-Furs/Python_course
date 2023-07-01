#Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. 
#Последняя строка содержит число X

from random import randint as rd
N = int(input("Введите количество элементов: "))
begin = int(input("Введите минимальное значение для заполнения списка: "))
end = int(input("Введите максимальное значение для заполнения списка: "))

numbers = list()
for i in range (N):
    numbers.append(rd(begin, end))
print (numbers)

x = int(input("Введите искомое число: "))

min = abs(x - numbers[0])
find_num = 0
for i in range(1, N):
        k = abs(x - numbers[i])
        if k < min:
            min = k
            find_num = i

print(f'Число {numbers[find_num]} в списке A наиболее близко по величине к числу {x}')
            


	