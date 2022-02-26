def adding(a, b):
    return a+b


if __name__ == '__main__':
    assert adding(1, 2) == 3
    assert adding(1, 0) == 1
    assert adding(0, 0) == 0
    print('Проверка прошла')
