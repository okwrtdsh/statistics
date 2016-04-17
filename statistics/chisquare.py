# -*- coding: utf-8 -*-
import math


def pdf(x, n):
    """
    カイ自乗分布の確率密度関数
    n=1, x->0で発散
    >>> pdf(0, 2)
    0.5
    >>> pdf(0, 3)
    0.0
    >>> pdf(0, 4)
    0.0
    >>> pdf(0, 5)
    0.0
    """
    return x**(n / 2.0 - 1.0) * math.exp(-x / 2.0) / (2.0**(n / 2.0) * math.gamma(n / 2.0))


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


def chisquare(v, alpha):
    """
    上側100alpha%点
    >>> chisquare(10, 0.05)
    18.30703813189708
    >>> chisquare(2, 0.99)
    0.020100671707434396
    """
    # FIXME: v=1のときは計算できない
    return binary_search(1.0 - alpha, f=lambda x: integration(lambda x: pdf(x, v), 0.0, x))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

