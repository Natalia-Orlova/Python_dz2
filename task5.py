# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random
n = int(input("Введите число: "))
list1 = list(range(0, n))
print(list1)
list2 = list()
for i in range(0, n):
    rand_idx = random.randrange(len(list1))
    list2.append(list1[rand_idx])
    list1.remove(list2[i])
print(list2)
