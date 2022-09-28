# 4. Напишите программу, которая принимает на вход 2 числа. Задайте список 
# из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

pos1 = int(input("Position 1: "))
pos2 = int(input("Position 2: "))
n = int(input("Number of elements: "))
if n <= 0 or pos1 <= 0 or pos2 <= 0:
    print ("Введено недопустимое значение, повторите попытку")
elif pos1 > n*2 + 1 or pos2 > n*2 + 1:
    print ("Номер позиции превышает количество элементов в списке")
else:
    lis = list()
    for i in range(-n, n+1):
        lis.append(i)
    print (lis)
    print(f"{lis[pos1-1]} * {lis[pos2-1]} = {lis[pos1-1] * lis[pos2-1]}")
