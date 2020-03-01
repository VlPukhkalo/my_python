def parity(a):
    '''Проверяет число на четность.

    >>> parity(10)
    1

    >>> parity(5)
    1
    '''

    if a%2==0:
        return 1
    else:
        return 0

import doctest
doctest.testmod()
