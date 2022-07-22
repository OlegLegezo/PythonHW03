'''Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''

# функция для создания и печати списка
def listZeroPlusN(resultArr=[]):
    n = int(input(
        'Введите положительное число N, для отображения всего промежутка 0 до N: '))
    # resultArr = []
    startValue = 0
    for i in range(0, n+1):
        resultArr.append(startValue)
        startValue += 1
        # print(sum)
    print(resultArr)
    return(resultArr)


Arr = []
listZeroPlusN(Arr)


# функция для перемножения крайних элементов списка

def listSumOddElements(inputArray=[]):
    answer = 0
    resultArr=[]
    if len(inputArray)%2==0:
        for i in range(int(len(inputArray)/2)):
            answer = inputArray[i]*inputArray[int(len(inputArray)-1)-i]
            resultArr.append(answer)
            #print(answer)
        i+=1
    else:
        for i in range(int(len(inputArray)/2)+1):
            answer = inputArray[i]*inputArray[int(len(inputArray)-1)-i]
            resultArr.append(answer)
            #print(answer)
        i+=1
    #print(answer)
    return(resultArr)
        #print(inputArray[i])

Arr2 = []
Arr2=listSumOddElements(Arr)

print(f'новый список состоящий из произведения пар чисел списка: {Arr2}')