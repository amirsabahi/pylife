def build_list(limit, list_type='even'):
    if list_type.lower() == 'even':
        return [i for i in range(limit) if i%2 == 0]
    elif list_type.lower() == 'odd':
        return [i for i in range(limit) if i%2 != 0]
    else: 
        raise TypeError('Invalid list type. It should be either odd or even.') 

print(build_list(20, 'even'))
print(build_list(20, 'odd'))

try:
    print(build_list(20, 'wrong type'))
except TypeError as exp:
    print(exp)    