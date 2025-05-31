import functools

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator called')
        result = func(*args, **kwargs)
        print('End of Decorator')
        return result
    return wrapper

@debug
def myfunc(name, family_name):
    print( f"{name} {family_name}")
    return f"{name} {family_name}"

myfunc('Shima', 'Nejati')