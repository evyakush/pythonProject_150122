
class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age





if __name__ == '__main__':
    tom_Cat = Cat('Tom', 3)
    print(tom_Cat)
    print(id(tom_Cat))
    print(f'{tom_Cat.name}, {tom_Cat.age}')
