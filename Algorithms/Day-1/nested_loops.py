""" Nested loops
"""


def nested_loops(seq):
    """ Nested loops.

    Args: seq(list/tuple)   A sequence of list or tuples
    """
    for segment_1 in seq:
        for segment_2 in seq:
            print(segment_1, "---->", segment_2)


if __name__ == "__main__":
    nested_loops([1, 2, 3, 4])
