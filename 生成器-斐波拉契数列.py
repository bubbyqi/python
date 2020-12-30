L = [ x*x for x in range(1,10)]
print(L)
g = ( x*x for x in range(1,10))
for n in g:
    print(n)


# 斐波拉契数列
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        # print(b)
        yield b
        a,b = b,a+b
        n = n + 1
    return 'done'

# print(fib(6))
for n in fib(6):
    print(n)
def odd():
    print('step1')
    yield 1
    print('step2')
    yield(3)
    print('step3')
    yield(5)

o = odd()
print(next(o))
print(next(o))
print(next(o))


