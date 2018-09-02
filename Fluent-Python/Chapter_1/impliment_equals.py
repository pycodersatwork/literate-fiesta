""" Impliment custom eq in python. This is essential to
    make user defined data structure behave the same way
    as builtin data structures.
"""


class Monkey:
    """ A specific group of monkeys.
    """
    def __init__(self, category):
        self.category = category

    def __eq__(self, animal):
        """ Check if the animal is in the same class of monkey.
        """
        if hasattr(animal, 'category'):
            return self.category == animal.category
        return False


if __name__ == "__main__":
    monkeyCategoryChimps = Monkey('chimp')
    monkeyCategoryLionTailed = Monkey('lion tailed')
    print(monkeyCategoryChimps == monkeyCategoryLionTailed)
    monkeyCategoryChimps_1 = Monkey('chimp')
    print(monkeyCategoryChimps == monkeyCategoryChimps_1)
