""" Named tuples and use in python.
"""

import collections


studentLibrary = collections.namedtuple('studentLibrary', 'rollNumber Name')


def loadStudentLibrary(students):
    """ Create a student library.

    Args: student (list)        List of students.

    Returns:
        (list)                  List of student record.
    """
    register = [
        studentLibrary(roll_no, name)
        for roll_no, name in enumerate(sorted(students), 1)
    ]

    return register


if __name__ == "__main__":
    students = ['Varadarajan', 'Arun', 'Ramachandran', 'Aditya']
    print(loadStudentLibrary(students))
