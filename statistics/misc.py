# -*- coding: utf-8 -*-


def integration(f, start, end, n=10**4):
    """
    積分 台形公式で近似
    >>> integration(lambda x: x, 0.0, 10.0)
    50.0
    >>> integration(lambda x: x**2, 0.0, 10.0)
    333.3333350000002
    """
    dx = (end - start) / n
    s = f(start) + f(end)
    for i in xrange(1, n):
        s += 2.0 * f(start + i * dx)
    s *= dx / 2.0
    return s


def binary_search(target, low=0.0, high=100.0, step=10**-12, f=lambda x: x):
    """
    二分探索
    >>> binary_search(2)
    1.9999999999993525
    >>> binary_search(2, f=lambda x: x**2)
    1.414213562372618
    """
    middle = (low + high) / 2.0
    while (low <= high):
        result = f(middle)
        if (target == result):
            break
        elif (target > result):
            low = middle + step
        elif (target < result):
            high = middle - step
        middle = (low + high) / 2.0
    return middle


if __name__ == "__main__":
    import doctest
    doctest.testmod()

