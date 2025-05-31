import functools


def debug(level):
    def debugger_level(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Debug level is {level}")
            print('Decorator called')
            resutl = func(*args, **kwargs)
            print('End of Decorator')
            return resutl
        return wrapper
    return debugger_level

@debug('error')
def myfunc(name, family_name):
    print( f"{name} {family_name}")
    return f"{name} {family_name}"

myfunc('Shima', 'Nejati')