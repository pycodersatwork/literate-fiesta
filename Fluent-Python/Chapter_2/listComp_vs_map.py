""" Experiment to check the speed of map vslist comps.
"""
import timeit


def wrapper(func, *args, **kwargs):
    """ A wrapper function for timeit to work with arguments.
    """
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def processStringUsingMap(inputStr):
    """ Get the ascii values of the input string.
    """
    return map(ord, inputStr)


def getAsciiUsingListComp(inputStr):
    """ Get the ascii value of the input string
        using list comprehension.
    """
    return [ord(i) for i in inputStr]


if __name__ == "__main__":
    print(processStringUsingMap('hello') == getAsciiUsingListComp('hello'))
    wrapperFunctionFromMap = wrapper(processStringUsingMap, 'hello')
    wrapperFunctionUsingListComp = wrapper(getAsciiUsingListComp, 'hello')
    print(timeit.timeit(wrapperFunctionFromMap, number=100000))
    print(timeit.timeit(wrapperFunctionUsingListComp, number=10000))
