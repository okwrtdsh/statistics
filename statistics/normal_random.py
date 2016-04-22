import random


def nrand():
    n = 0.0
    for _ in xrange(12):
        n += random.random()
    return n - 6.0


def normal_random(n, use_default=True):
    if use_default:
        r = (random.normalvariate(mu=0, sigma=1) for _ in xrange(n))
    else:
        r = (nrand() for _ in xrange(n))
    return r

