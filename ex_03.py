'''
Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

from cgi import print_arguments


Arr2 = [1.1, 1.2, 3.1, 5, 10.01]


import random as rnd


# метод для поиска макс и мин дробной части (отбрасывая числа без дробной части)
def difMaxMin(Arr1):
      max = round((Arr1[0] - int(Arr1[0])), 4)
      min = round((Arr1[0] - int(Arr1[0])), 4)
      for i in range(int(len(Arr1))):
            now = round((Arr1[i] - int(Arr1[i])), 4)
            if now != 0:
                  if now>max:
                        max=now
                  if now<min:
                        min=now
                  
      print(f'разница между максимальным ({max}) и минимальным ({min}) значением дробной части элементов: {round((max-min), 4)}')


print(f'массив из примера: {Arr2}')
difMaxMin(Arr2)

# генерация массива из случайных чисел
lenArr = int(input('Введите длину списка для генерации списка: '))
arr = [round(rnd.randint(1, 10) * rnd.random(), 2) for _ in range(lenArr)]
print(arr)
difMaxMin(arr)




# далее мои заметки
'''



# a = input("Введите вещественное число: ").split('.')
# # Введите вещественное число: 15.155441514
# print(a[0])
# if a[1]>0:
#       print(a[1])
# # print(a[2])
# # print(a[0] == a[1][:2])
# True

# x = 1
# print(x % 1)
# print(round((x - int(x)), 4))


# x.is_integer()

# import math
# x = float(input())
# y = x-math.floor(x)
# print(y)
'''