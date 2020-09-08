def IAmDecorator(fun):
    def wrapper(*args, **kwargs):
        print('我是一个装饰器')
        return fun
    return wrapper

@IAmDecorator
def func(h):
    print('我是被装饰函数')

func()(h=1)
print(func.__name__)