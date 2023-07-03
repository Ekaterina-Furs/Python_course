'''Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 '''

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
def degree(num, exponent):
    if exponent == 1:
        return num
    if exponent == 0:
        return 1
    else:
        return(num * degree(num, exponent - 1))
print("Результат равен:",degree(A,B))