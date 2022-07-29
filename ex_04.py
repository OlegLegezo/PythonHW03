'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''

# функция для перерасчета 10тичного числа в двоичное

n = int(input('Введите положительное десятичное число N: '))


def tenConvertBool(input,list=[]):
    result = 0
    a = int(input/2)
    # print(a)
    if a>0:
        if input % 2 == 0:
            result = 0        
            list.insert(0,result)
        else:
            result = 1
            list.insert(0,result)
        # list.insert(0,a)
        tenConvertBool(a,list)
    else:
        list.insert(0,input)
        # print(list)
        print(f'двоичное число:')
        for i in list:
            print(i,end = '')

    return(list)


tenConvertBool(n)
