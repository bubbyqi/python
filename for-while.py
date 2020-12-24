names = ['Michael','Bob','Tracy']
for name in names:
    print(name)


sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

print(list(range(101)))


sum = 0
for x in (list(range(101))):
    sum = sum + x
print(sum)


sum = 0
i = 99
while i > 0:
    sum = sum + i
    i = i-2
print(sum)

L = ['Bart','Lisa','Adam']
for i in L:
    print('hello',i)

n = 1
while n <=100:
    print(n)
    n = n+1

n = 1 
while n <= 100:
    print(n)
    n = n + 1
    if n > 10:
        break

n = 0 
while n < 100:
    n = n+1
    if n % 2 ==0:
        continue
    print(n)