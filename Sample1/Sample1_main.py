#
# def sq_1():
#     return x**3
# result = lambda x, y: x*y
# result2 = lambda: x**2
# if __name__ == '__main__':
#     print(result(3, 5))
#     x = 1000
#     print(result2())
#     print(sq_1())


ivan = {
    'city': 'Vlad',
    'car': 'Prado'
    }
denis = {
    'city': 'Vlad',
    'car': 'Carina'
    }
oleg = {
    'city': 'Mos',
    'car': 'BMW'
    }
persons = [ivan, denis, oleg]

# cars = []

# for person in persons:
#     # print(person['car'])
#     cars.append(person['car'])
#     # print(cars)
#     # cars.append(persons[person])

new_cars = [person['car'] for person in persons]
new_city = [person['city'] for person in persons]

squares = [i**2 for i in range(100) if i % 3 == 0]


if __name__ == '__main__':
    # print(cars)
    print(new_cars)
    print(new_city)
    print(squares)
    print('text')

