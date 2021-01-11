# def createCounter():
#     a = 0
#     def counter():
#         nonlocal a
#         a = a + 1
#         return a
#     return counter

# def createCounter():
#     c = [0]
#     def counter():
#         c[0]+=1
#         return c[0]
#     return counter

# def createCounter():
    
#     def iterator():
#         n = 1
#         while True:
#             yield n
#             n += 1
#     g = iterator()
#     def counter():
#         return next(g)
#     return counter

def createCounter():
    count = []
    def counter():
        count.append(1)
        return len(count)
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')