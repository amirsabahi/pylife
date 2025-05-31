import functools
class Debug:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        
    def __call__(self, *args, **kwargs):
        print('Debug logic here')
        return self.func(*args, **kwargs)
    
@Debug
def say_hello(name):
    print(f"Hey {name},")
    return None

say_hello('Max')