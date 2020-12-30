L = list(range(1,11))
print(L)
# t = []
# for i in L:
#     t.append(i*i)
t = [x*x for x in range(1,11) if x % 2 == 0]

print(t)
t = [ x*x for x in range(1,11)]
print(t)
t = [ x+y for x in ['A','B','C'] for y in 'XYZ']
print(t)
d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)

l = [x for x in range(1,101) if x % 2 == 0]
print(l)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 =  [s.lower() if isinstance(s,str) else s for s in L1 ]
print(L2)