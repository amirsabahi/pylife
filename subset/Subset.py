from collections import Counter


class Subset:
    set1 = set2 = set()

    def __init__(self, set1, set2):

        self.set1 = set(set1)
        self.set2 = set(set2)

    def isSubset(self):
        counter_set1 = Counter(self.set1)
        counter_set2 = Counter(self.set2)
        print(counter_set1)
        print(counter_set2)

        for key in counter_set2:
            if counter_set2[key] > counter_set1[key]:
                return False
            if key not in counter_set1:
                return False
        return True


s = Subset([1340, 1647, 2844, 3848], [167, 3848])

print(s.isSubset())

s = Subset([1340, 1647, 2844, 3848], [1647, 3848])

print(s.isSubset())