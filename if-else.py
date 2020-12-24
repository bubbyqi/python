age = int(input('please input your age:'))
if age >= 18:
    print('your age is',age)
    print('adult')
elif age>=6:
    print('your age is',age)
    print('teenger')
else:
    print('your age is',age)
    print('kid')

height = float(input('please input your height:'))
weight = float(input('please input your weight:'))
bmi =  weight/(height**2)
if bmi<18.5:
    print('too low')
elif 18.5<bmi<25:
    print('normal')
elif 25<bmi<28:
    print('too high')
elif 28<bmi<32:
    print('肥胖')
else:
    print('严重肥胖')