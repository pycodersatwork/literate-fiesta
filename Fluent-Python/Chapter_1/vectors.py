""" Simple vectors.
"""

from math import hypot


class Vectors:
    """ A simple vector class.
    """
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def __add__(self, other):
        """ Adding two points in space.
        """
        if all([hasattr(other, attr) for attr in ('point_1', 'point_2')]):
            self.point_1 = self.point_1 + other.point_1
            self.point_2 = self.point_2 + other.point_2

        return Vectors(self.point_1, self.point_2)

    def __abs__(self):
        """ Get the absolute value of the vector in space.
        """
        return hypot(self.point_1, self.point_2)

    def __repr__(self):
        """ Represent the class.
        """
        return "{vector}".format(vector=self.__class__.__name__)



if __name__ == "__main__":
    vector1 = Vectors(0, 0)
    vector2 = Vectors(3, 4)
    print(abs(vector2))
    vector3 = vector1 + vector2
    print(abs(vector3))