
# def sterngth_pass(value):
#     if len(value) < 8:
#         print('from function')
#         return "weak pass"
#     return 'Print'
def divide_num(a,b):
    try:
        aa = a/b
        return aa
    except ZeroDivisionError:
        # print("Деление на ноль")
        return 'Divide by zero'
if __name__ == '__main__':
    # assert sterngth_pass(' ')
    print(divide_num(1,0))