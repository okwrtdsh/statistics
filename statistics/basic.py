import math


class Statistics(object):
    _total = None
    _length = None
    _mean = None
    _variance = None
    _stdev = None

    def __init__(self, data):
        """
        >>> Statistics([1, 2, 3, 4, 5]).data
        [1.0, 2.0, 3.0, 4.0, 5.0]
        """
        self.data = map(float, data)

    @property
    def total(self):
        """
        >>> Statistics([1, 2, 3, 4, 5]).total
        15.0
        """
        if self._total is None:
            self._total = float(sum(self.data))
        return self._total

    @property
    def length(self):
        """
        >>> Statistics([1, 2, 3, 4, 5]).length
        5.0
        """
        if self._length is None:
            self._length = float(len(self.data))
        return self._length

    @property
    def mean(self):
        """
        >>> Statistics([1, 2, 3, 4, 5]).mean
        3.0
        """
        if self._mean is None:
            self._mean = self.total/self.length
        return self._mean

    @property
    def variance(self):
        """
        >>> Statistics([1, 2, 3, 4, 5]).variance
        2.0
        """
        if self._variance is None:
            self._variance = float(sum((i-self.mean)**2 for i in self.data)) / self.length
        return self._variance

    @property
    def stdev(self):
        """
        >>> Statistics([1, 2, 3, 4, 5]).stdev
        1.4142135623730951
        """
        if self._stdev is None:
            self._stdev = math.sqrt(self.variance)
        return self._stdev

if __name__ == "__main__":
    import doctest
    doctest.testmod()

