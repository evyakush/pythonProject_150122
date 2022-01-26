a = '$' # expression
allowed = '+-*/' # перечень того, что проверяем

while True:
    if a in allowed:
        print('OK')
    else:
        print('Ни одного совпадения Not Found')
    a = input('Введите свой знак')
    if a == 'bp':
        print('Завршил программу')
        break


# for i in allowed: # сам цикл проверки
#     if a in i:
#         print('OK')
#         break
#     else:
#         print('No Good')
#     print('Ни одного совпадения')
# print('Проверка выполнена')