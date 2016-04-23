# -*- coding: utf-8 -*-
import math
from misc import integration


def pdf(x, mu=0.0, sigma=1.0):
    """
    正規分布の確率密度関数
    >>> pdf(0)
    0.3989422804014327
    >>> pdf(1)
    0.24197072451914337
    """
    return math.exp(-((x - mu)**2.0) / (2.0 * sigma**2.0)) / (((2.0 * math.pi)**0.5) * sigma)


def normal(zscore):
    """
    下側確率
    >>> normal(0.0)
    0.5
    >>> normal(3.09)
    0.9989992174405429
    >>> normal(-3.09)
    0.0010007825594570696
    """
    if zscore >= 0:
        return 0.5 + integration(pdf, 0.0, zscore)
    return 0.5 - integration(pdf, 0.0, math.fabs(zscore))


if __name__ == "__main__":
    import doctest
    doctest.testmod()

