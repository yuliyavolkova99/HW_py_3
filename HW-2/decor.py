#задание 1
def log(func):
    def inner(*args, **kwargs):
        print(f'Вы вызвали функцию {func.__name__}{args}')
        print(f'Она вернула значение {func(*args, **kwargs)}')
        return func(*args, **kwargs)
    return inner

@log
def function(*args):
    return 3 + len(args)


print(function(4, 4, 4))

#задание 2
from datetime import *
def html(func):
    def wrapper(*args, **kwargs):
        ans = func(*args, **kwargs)
        date = datetime.now().strftime("%Y/%m/%d %H:%M")
        with open('my_file.html','w') as f:
            f.write(f'{date} \n <html><strong>{ans}</strong></html>')
        return ans
    return wrapper

@html
def function(s = "hello"):
    return s

function('hi')
