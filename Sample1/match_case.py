def calculator(a,b,calcul):
    match calcul:
        case '+':
            return a+b
        case '-':
            return a-b
        case '*':
            return a*b
        case '/':
            return a/b


if __name__ == '__main__':
    print(calculator(2, 3, '+'))
    print(calculator(2, 3, '-'))
    print(calculator(2, 3, '*'))
    print(calculator(2, 3, '/'))

