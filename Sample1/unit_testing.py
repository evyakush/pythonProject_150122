
allowed = '+-*/' # перечень того, что проверяем

#
# item_list = [1, 2, 3, 4, 5, 6]
# print (all(item > 2 for item in item_list))
# print ([item > 2 for item in item_list])
# print (any(item > 2 for item in item_list))
# print ([item > 2 for item in item_list])

def check_ex(expression):
    if not any(check_simb in expression for check_simb in allowed):
        print('No good')
check_ex('$')

while True:
    a = input('Введите свой знак, комбинация bp выход из программы')

    if a == 'bp':
        print('Завершил программу')
        break

    if a in allowed:
        print(f'Ты ввел символ ({a}) он находится в  заданной последовательности, OK')
    else:
        print('Ни одного совпадения не найдено')





