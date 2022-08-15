import functools

'''
Sometimes I need to remember a function return value for the same arguments. I use this function to achieve this.
'''


def memo(function):
    # The functools module is for higher-order functions: functions that act on or return other functions.
    # https://docs.python.org/3/library/functools.html?highlight=functools

    cache = {}

    @functools.wraps(function)
    def wrapper(*args):
        if args in cache:
            print('Use my memory')
            return cache[args]

        call_result = function(*args)

        print('Calling %s()' % function.__name__)
        cache[args] = call_result
        return call_result

    return wrapper


@memo
def my_pow(x):
    return x * x


print('result: %d' % my_pow(8))
print('result: %d' % my_pow(12))
print('result: %d' % my_pow(8))
