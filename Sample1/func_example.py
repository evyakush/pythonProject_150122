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
ex_list = list(range(0,3))
print(ex_list)
ww = [[list(range(x, x+3))] for x in range(3)]

print(ww)

if __name__ == '__main__':
    print(simple_func)
    print('Проверка')

    print('Проверка 2')
    print('Проверка3')
    print("Проверка4")
    print("Проверка 5 с работы")
    # text = input("Введите ваш текст")
    # print(f'Ввы ввели текст {text}')