'''
17. задайте список из n элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся в file.txt, одно число - одна строка
'''

# import random
# n = int(input())
# mult = 1
# some_list = [random.randint(-n, n) for _ in range(n)]
# print(some_list)
# with open('file.txt', 'w+', encoding='utf-8') as file:
#     count = random.randint(1, n)
#     for _ in range(count):
#         file.write(f'{random.randint(0, n - 1)}' + '\n')
#         file.seek(0, 0)
#         index_list = file.read().splitlines()
#     for index in index_list:
#         mult = mult * some_list[int(index)]
# print(mult)


'''Напишите функцию, которая принимает номер месяца и язык (русский или английский), а возвращает его название.
Ввод:
print(month_name(3, "en"))
March
Ввод
print(month_name(3, "ru"))
Март
'''

# def mounth(x, y):
#     listEn = ('January', 'February', 'March', 'April', 'May', 'June',
#     'July', 'August', 'September', 'October', 'November', 'December')
#     listRu = ('январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
#     'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь')
#     if x > 0 and x < 13:
#         if y == 'en':
#              return listEn[x-1]
#
#         if y == 'ru':
#             return listRu[x-1]
#
# print(mounth(11,'en'))