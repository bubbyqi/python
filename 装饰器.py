def now():
    print('2021-1-11')
f = now
print(f.__name__)

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2021-1-11')
print(now())

import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2021-1-11 13:39')
print(now())

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
             print('%s %s():' % (text,func.__name__))
             return func(*args,**kw)
        return wrapper
    return decorator

@log('excute')
def now():
    print('2021-1-11 13:42')
print(now())