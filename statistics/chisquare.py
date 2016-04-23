# -*- coding: utf-8 -*-
import math
from misc import integration, binary_search


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

