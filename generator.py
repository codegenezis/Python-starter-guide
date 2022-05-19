list = [1,2,3,4]
def func():
    for i in list:
        print(i)
        yield

obj = func()

next(obj)
next(obj)
next(obj)