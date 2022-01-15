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
print(simple_func)
print('Проверка')
print('Проверка 2')
print('Проверка3')
print("Проверка4")
print("Проверка 5 с работы")