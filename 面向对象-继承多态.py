class Animal(object):
    def run(self):
        print('animal is running!')

class Dog(Animal):
    # pass
    def run(self):
        print('Dog is running')

class Cat(Animal):
    # pass
    def run(self):
        print('Cat is running')

dog = Dog()
cat = Cat() 
# dog.run()
# cat.run()

a = list()
b =  Dog()
c = Cat()
print(isinstance(a,list))
print(isinstance(b,Dog))
print(isinstance(c,Cat))

print(isinstance(c,Animal))