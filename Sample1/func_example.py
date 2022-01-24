# def simple_func():
#     print('It,s simple func')

def big_func(func):
    print('From big func')
    def wrop_func():
        print('befor wrop func')
        func()
        print('after wrop')
    return wrop_func

# simple_func()
#
# simple_func = big_func(simple_func)
# simple_func()

@big_func
def simple_func():
    print('It,s simple func')




simple_func()
a = 2 #Добавлено просто, чтобы внести изменения в код.

aa = [x for x in range(0, 2)]
# print(aa)
w = [[x for x in (x, x, x)] for x in range(0, 4)]
print(w)
ex_list = list(range(0, 3))
print(ex_list)
ww = [[list(range(x, x+3))] for x in range(3)]
a_data = 'ddddddddddaaaaaaasdasdasd'
a_dict = {e: b for e, b in enumerate(a_data)}
a_gen = (a**2 for a in range(1, 100) if a % 2 == 0)
print(a_gen)

for i in a_gen:
    print(i)



print(ww)
ab = 'abcdefijk'
ab_dict = {a : b for a, b in enumerate(ab)}
print(ab_dict)
print(type(ab_dict))
a_triple = [a**3 for a in range(0, 11) if a % 2 == 0]
print(a_triple)
a_quad = (a**3 for a in range(0, 11) if a % 2 == 0)
print()
print(a_quad)
for i in a_quad:
    print(i)

if __name__ == '__main__':
    print(simple_func)
    print('Проверка')

    print('Проверка 2')
    print('Проверка3')
    print("Проверка4")
    print("Проверка 5 с работы")
    # text = input("Введите ваш текст")
    # print(f'Ввы ввели текст {text}')
    print(f'Это то что нужно {a_dict}')
    print(type(a_dict))
    print({a: e for a, e in a_dict.items()})