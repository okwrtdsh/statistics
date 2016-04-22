# -*- coding: utf-8 -*-
import math
from .misc import integration


def pdf(x, mu=0.0, sigma=1.0):
    """
    正規分布の確率密度関数
    """
    return math.exp(-((x - mu)**2.0) / (2.0 * sigma**2.0)) / (((2.0 * math.pi)**0.5) * sigma)


def normal(zscore):
    """
    下側確率
    """
    if zscore >= 0:
        return 0.5 + integration(pdf, 0.0, zscore)
    return 0.5 - integration(pdf, 0.0, math.fabs(zscore))

