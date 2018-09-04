""" Loops.
"""


def loops(seq):
    """ Simple execution of for loop.

    Args: seq (list)    Sequence of elements.
    """
    for _ in seq:
        print("Hello World")


if __name__ == "__main__":
    loops((1, 2, 3, 4, 5))
