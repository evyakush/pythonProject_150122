#
# allowed = '+-*/' # перечень того, что проверяем
#
# while True:
#     a = input('Введите свой знак, комбинация bp выход из программы')
#
#     if a == 'bp':
#         print('Завершил программу')
#         break
#
#     if a in allowed:
#         print(f'Ты ввел символ ({a}) он находится в  заданной последовательности, OK')
#     else:
#         print('Ни одного совпадения не найдено')
#
# 
from functools import reduce
#
# sizes = input('Введите три значения')
# print(sizes)
# print(type(sizes))
# sizes = sizes.split()
# print(type(sizes))
# print(sizes)
# x, y, zx, y, z = map(int, input('Введите еще три значения').strip().split())
# print(f'{x=} , {y = }, {z= }')

volume_reduce = reduce(lambda x, y: x*y, map(int, input('Введите еще три значения').strip().split()))
print(volume_reduce)
names_list = ["Иван", "Прохор", "Илья", "Анастасия", "Альбина"]
name_start_letter =[nm_letter for nm_letter in names_list if nm_letter.startswith("П")]
print(name_start_letter)

