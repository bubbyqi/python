class Student(object):
    # pass
    __slots__=('name','age')

s = Student()
s.name = 'bubby'
s.age = '34'
s.gender =  'fmale'
print(s.name)
print(s.age)
print(s.gender)
# def set_age(self,age):
#     self.age=age
# from types import MethodType
# s.set_age = MethodType(set_age,s)
# s.set_age(25)
# print(s.age)

# s2 = Student()
# s2.set_age(25)
# print(s2.age)
