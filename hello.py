from collections import Iterable, Iterator, Container
li = ['1','2','3']
li_iter = iter(li)
print(isinstance(li,Iterator))
print(isinstance(li_iter,Iterator))
print(next(li_iter))