Built-in sequences in python
- Container sequences
    + list, tuples and collections.deque
- Flat sequences
    + str, bytes, bytearray, memoryview and array.array

Another way of grouping sequences
- Mutable sequence
    + list, bytearray, array.array, memoryview and collections.deque
- Immutable sequences
    + tuples, str, bytes


#### When should you use a namedtuple?
- [namedtuple as an ideal solution](https://stackoverflow.com/questions/9872255/when-and-why-should-i-use-a-namedtuple-instead-of-a-dictionary)

#### Some key attributes/function worth noting for named tuple are
- _asdict()
- _fields
- _make()


#### Augmented assignment with sequences
- Augmented assignment operators are += and *=. They are implemented using
    + _iadd
    + _imul
If the augmented assignment operator is not implemented then the operation
falls back to a = a + b. 
*It is to be noted that its always better to implement augmented operation
to mutable sequences. *

To visualize the python data structures
- [Online python tutor](http://pythontutor.com/visualize.html#mode=display) 
