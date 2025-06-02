def calculate_daily_return(values:list)->float:
    for i in range(1, len(values)):
        if values[i-1] == 0:
            raise ZeroDivisionError('First value can not be 0')
        yield ((values[i]-values[i-1])/values[i-1])*100

print(list(calculate_daily_return([1000, 1020, 1010])))