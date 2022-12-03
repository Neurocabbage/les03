'''1. Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''

# List = [2, 3, 67, 4, 34, 5, -45, 3]
# print(List)
# Sum=0
# for i in range(len(List)):
#     if i % 2 != 0:
#         Sum += List[i]
# print(Sum)

'''2. Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''

# List = [2, 3, 67, 4, 34, 5, -45]
# print(List)
# MultList = []
# for i in range(len(List)//2+1):
#     MultList.append(List[i]*List[-i-1])
# print(MultList)


'''Задайте список из вещественных чисел. Напишите программу, 
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''

# List = [2.34, 3.34, 67.02, 4.9, 34.2, 5.4, -45.01]
# print(List)
# MinFractional = abs(List[0]) % 1
# MaxFractional = abs(List[0]) % 1
# for i in range(len(List)):
#     if abs(List[i])%1< MinFractional:
#         MinFractional = abs(List[i])%1
#     if abs(List[i])%1> MaxFractional:
#         MaxFractional = abs(List[i])%1
# print(MaxFractional-MinFractional)

'''Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10'''

# dec_num = int(input('Введите число: '))
# # чтобы сохранить исходное число для конечного вывода поместил преобразование в функцию
# def FromDecToBin(dec_num):
#     bin_num = ''
#     while dec_num > 0:
#         bin_num = str(dec_num%2) + bin_num
#         dec_num= dec_num//2
#     return bin_num
# print(dec_num, ' -> ', FromDecToBin(dec_num))

'''Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)
'''
num = int(input('Введите число: '))

def fib(n: int) -> list:
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    li = fib(n-1)
    li.append(li[-1] + li[-2])
    return li

List = fib(num)
for i in range(len(List)):
    List.insert(0, List[i+i]*(-1))
List.insert(num, 0)
print(List)



