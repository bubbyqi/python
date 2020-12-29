
print(abs(100))
print(abs(-10))
print(max(1,23,4,5,6,8,9,13))
a = abs
print(a(-1))
n1 = 255
n2 = 1000
print(hex(n1),hex(n2))

def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-99))

def nop():
    pass

def power(x):
    return x * x
print(power(5))

def enroll(name,gender):
    print('name:',name)
    print('gender:',gender)
enroll('Sarah','F')

def enroll(name,gender,age=6,city='Shanghai'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
enroll('Sarah','F')

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc(1,2)