L = list(map(lambda x: x*x,[1,2,3,4,5,6,7,8,9]))
print(L)

def build(x,y):
    return lambda : x*x+y*y

L = build(1,2)
print(L())


L = list(filter(lambda x: x%2==1,range(1,20)))
print(L)