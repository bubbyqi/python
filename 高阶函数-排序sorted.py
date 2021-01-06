L = sorted([36,5,-12,9,-21])
print(L)
L = sorted([3,43,9,-50,-345],key=abs)
print(L)
L = sorted(['bob','about','Zoo','Credit'],key=str.lower)
print(L)
L = sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True)
print(L)
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    return t[1]

L2 = sorted(L,key=by_score,reverse=True)
print(L2)