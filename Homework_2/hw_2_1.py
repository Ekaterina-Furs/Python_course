#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки 
#были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
#которые нужно перевернуть


num = int(input("Введите количество монет и введите их положение (монета-решка  = 0, монета-герб  = 1): "))
count = 0
for i in range(num):
    value = int(input())         
    if value == 1:
        count += 1
if count < num/2:
    print(count)
else:
    print (num-count)

