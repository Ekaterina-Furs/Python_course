'''В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
 Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и 
нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.'''

from random import randint as rd
num = int(input("Введите количество кустов : "))
begin = int(input("Введите минимальное значение урожайности (ягод): "))
end = int(input("Введите максимальное значение урожайности (ягод): "))
list_berries = list(rd(begin, end) for i in range(1,num+1))
print("Урожайность с кустов:",list_berries)

first_bush = int(input("Введите начальную позицию (номер куста): "))
res = 0
if first_bush == 1:
    res =  list_berries[0] + list_berries[1] + list_berries[-1]
elif first_bush == len(list_berries):
    res = list_berries[-2] + list_berries[-1] + list_berries[0]
else:
    res = list_berries[first_bush-1] + list_berries[first_bush-2] + list_berries[first_bush]
print("Максимальное число сбора:", {res}, "ягод за один заход")
