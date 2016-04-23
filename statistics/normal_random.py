# -*- coding: utf-8 -*-
import random


def nrand():
    n = 0.0
    for _ in xrange(12):
        n += random.random()
    return n - 6.0


def normal_random(n, mu=0.0, sigma=1.0, use_default=True):
    if use_default:
        r = [random.normalvariate(mu=mu, sigma=sigma) for _ in xrange(n)]
    else:
        r = [mu + sigma * nrand() for _ in xrange(n)]
    return r

