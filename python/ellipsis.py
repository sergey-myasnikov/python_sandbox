"""
Three dots (...) or Ellipsis in Python 3.

"""

import numpy as np
import doctest

from typing import Callable


def ellipsis_type():
    """
    Ellipsis can be assigned to variables
    Ellipsis type is 'ellipsis'
    Ellipsis is a singleton object
    """
    x = ...
    y = ...

    print(None is ...)

    print(f"x is {x}")  # Ellipsis
    print(f"x type is {type(x)}") # <class 'ellipsis'>
    print(x.__dir__())

    print(x is ...)  # True
    print(x is Ellipsis)  # True
    print(x is y)  # True

    print(f"bool of Ellipsis is always {bool(Ellipsis)}")

    print({x, y})  # {Ellipsis}
    print({x: "x", y: "y"})  # {Ellipsis: 'y'}


def placeholder():
    """
    1. Ellipsis as a placeholder (Like pass)
    """
    ...
    try:
        if True:
            ...
    except Exception:
        ...
    ...

def ellipsis_array_slicing():
    """
    2. Multidimensional Array Slicing (NumPy)
    Explanation:
        np.random.rand(2, 2, 2, 2) creates a 4D array with random values and shape (2, 2, 2, 2).
        a[..., 0] slices the array, selecting the first element along the last axis, resulting in shape (2, 2, 2).
        ... replaces the number of colons (:) needed to fill missing axes
        a[Ellipsis, 0] is equivalent to a[..., 0],
            explicitly including all preceding dimensions and producing the same shape.
    """
    a = np.random.rand(2, 2, 2, 2)

    # Fix the last dimension
    print(a[..., 0])        # Same as a[:, :, :, 0]
    print(a[Ellipsis, 0])   # Same as a[..., 0] and a[:, :, :, 0]

    # Fix the first dimension
    print(a[0, ...])        # Same as a[0, :, :, :]

    # Fix the first and the last dimensions
    print(a[0, ..., 0])     # Same as a[0, :, :, 0], resulting in shape (2, 2)

    # Cannot use 2 ellipsis because of
    # IndexError: an index can only have a single ellipsis ('...')
    try:
        print(a[..., 0, 0, ...])
    except IndexError:
        ...

def type_hinting_1() -> tuple[int, ...]:
    """
    3.1 Type hinting
    Tuple of ints of any length
    """
    return 1,


def type_hinting_2(data: ...):
    """
    3.2 Type hinting
    Unknown parameter type
    """
    print(data)

def type_hinting_3(some_function: Callable[..., str]) -> ...:
    """
    3.3 Type hinting with callable
    some_function can be any callable that takes any arguments and returns a string.
    """
    s:str = some_function()
    return s

def default_argument_value(x=...):
    """
    4. Default Argument value.
    (other than None, etc.)
    """
    if x is Ellipsis:
        print("No value provided")
    else:
        print(f"Value: {x}")

def repl_in_doctest():
    """
    5. Interpreter Prompt (REPL)
    Not an ellipsis.
    In Python's interactive shell (REPL), ... is used as a secondary prompt
        to indicate that the interpreter is expecting more input.

    Example in doctest:
    >>> for i in range(3):
    ...     print(i)
    0
    1
    2
    """
    ...

# In .pyi (Python Interface) stub files
def stub_function() -> bool: ...


if __name__ == '__main__':

    ellipsis_type()
    print(placeholder())  # None

    ellipsis_array_slicing()

    print(type_hinting_1())
    type_hinting_2("some data")

    default_argument_value()
    default_argument_value(1)
    default_argument_value(None)
    default_argument_value("test")

    doctest.testmod()  # run doctest with ... in repl_in_doctest()
    print("Doctest with ... passed")
