from collections import Counter

def count_frequency(str: str)->dict:
    return dict(Counter(str))

print(count_frequency('aaabbdhSDwe4erewvcvxc'))