def findMinAndMax(L):
    if not L:
        return (None,None)
    max=min=L[0]
    for i in L:
        if i > max:
            max = i
        if i < min:
            min = i
    return (max,min)
L = list(range(100))
t = findMinAndMax(L)
for i in t:
    print(i)
print(t)
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')