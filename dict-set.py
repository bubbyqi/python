names = ['Micheal','Bob','Tracy']
scores = [90,80,70]
d = {'Micheal':90,'Bob':80,'Tracy':70}
print(d['Micheal'])
d['Adm']='60'
print(d['Adm'])
print(d)
print('Adm' in d)
print('Micheal score is:',d['Micheal'])
d.pop('Bob')
print(d)
s = set([1,2,3])
print(s)
s = set([1,2,2,3,3,4,5])
print(s)
s = set([1,2,3,3,4,5])
s.add(5)
s.add(6)
print(s)
s.remove(6)
print(s)





