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