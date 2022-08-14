import abc


class Bird(abc.ABC):
    def lay_egg(self):
        pass


class Chicken(Bird):
    def lay_egg(self):
        # A Chicken lays an egg that will hatch into a new Chicken.
        return Egg(Chicken)


class Egg:
    hatchCount = 0
    bird = None

    def __init__(self, bird):
        self.bird = bird

    def hatch(self):
        if self.hatchCount > 0:
            raise NameError(' Hatched already! ')  # Hatching an egg for the second time throws an Exception
        self.hatchCount += 1
        return self.bird()  # Eggs from other types of birds should hatch into a new bird of their parent type.


'''
Run
'''
chick_one = Chicken()
first_egg = chick_one.lay_egg()

# Now we have another chick here
chick_two = first_egg.hatch()
print(chick_two)
print('Now we have new chick form the first chicken.\n')

another_egg = chick_two.lay_egg()
third_chick = another_egg.hatch()  # Voilà we have a new bird now!
print('Voilà we have a new bird now!\n')

# Can we another_egg hatch again? No!
try:
    another_egg.hatch()
except Exception as e:
    print(e)
