
def password_strength(passwd: str) -> str:
    print('From func')


if __name__ == '__main__':
    assert password_strength('') == 'Too weak'
    assert password_strength(123567) == 'Too weak'