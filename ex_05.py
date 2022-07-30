'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
'''


# функция для создания и печати списка Фибоначчи
def listFibPos(n=int, resultArr=[]):

    resultArr = [0, 1]
    for i in range(2, n+1):
        resultArr.append(resultArr[i-1]+resultArr[i-2])
    # print(resultArr)
    return(resultArr)


n = int(input(
    'Введите положительное число N (больше 1), для отображения Негафибоначчи: '))


Arr = []
# Arr = listFibPos(n, Arr)
# print (Arr)



# функция для создания и печати списка Негафибоначчи
def listFibNeg(n=int, resultArr=[]):
    j = 1
    for i in range(1, n+1):
        if i % 2 == 0:
            resultArr.insert(0, resultArr[j]*(-1))
        else:
            resultArr.insert(0, resultArr[j])
        j = j+2
    print(resultArr)
    return(resultArr)


Arr = listFibNeg(n, listFibPos(n, Arr))
# print (Arr)
