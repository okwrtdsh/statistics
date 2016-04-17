# -*- coding: utf-8 -*-
import math


class Statistics(object):
    _total = None
    _length = None
    _mean = None
    _variance = None
    _stdev = None
    _classes = None
    _frequency = None

    def __init__(self, data, bins=None, bin_width=None):
        """
        >>> Statistics([1, 2, 3, 4, 5]).data
        [1.0, 2.0, 3.0, 4.0, 5.0]
        """
        self.data = map(float, sorted(data))
        self._bins = bins
        self._bin_width = bin_width

    @property
    def total(self):
        """
        合計
        >>> Statistics([1, 2, 3, 4, 5]).total
        15.0
        """
        if self._total is None:
            self._total = float(sum(self.data))
        return self._total

    @property
    def length(self):
        """
        個数
        >>> Statistics([1, 2, 3, 4, 5]).length
        5.0
        """
        if self._length is None:
            self._length = float(len(self.data))
        return self._length

    @property
    def mean(self):
        """
        平均値
        >>> Statistics([1, 2, 3, 4, 5]).mean
        3.0
        """
        if self._mean is None:
            self._mean = self.total / self.length
        return self._mean

    @property
    def variance(self):
        """
        分散
        >>> Statistics([1, 2, 3, 4, 5]).variance
        2.0
        """
        if self._variance is None:
            self._variance = float(
                sum((i - self.mean)**2 for i in self.data)) / self.length
        return self._variance

    @property
    def stdev(self):
        """
        標準偏差
        >>> Statistics([1, 2, 3, 4, 5]).stdev
        1.4142135623730951
        """
        if self._stdev is None:
            self._stdev = math.sqrt(self.variance)
        return self._stdev

    @property
    def bins(self):
        """
        階級数
        Sturges' formulaを利用
        """
        if self._bins is None:
            self._bins = int(math.ceil(1 + (math.log(self.length, 10) / math.log(2, 10))))
        return self._bins

    @property
    def bin_width(self):
        """
        階級幅
        """
        if self._bin_width is None:
            self._bin_width = int(math.ceil((self.data[-1] - self.data[0]) / float(self.bins)))
        return self._bin_width


    @property
    def classes(self):
        """
        階級の上限値のリスト
        """
        if self._classes is None:
            result = []
            for i in xrange(self.bins + 1):
                if i == 0:
                    result.append(self.data[0] + 0.5)
                else:
                    result.append(result[i-1] + self.bin_width)
            self._classes = result
        return self._classes

    @property
    def frequency(self):
        """
        度数分布表
        """
        if self._frequency is None:
            result = {c:[] for c in self.classes}
            i = 0
            for c in self.classes:
                while i < self.length and self.data[i] < c:
                    result[c].append(self.data[i])
                    i += 1
            self._frequency = result
        return self._frequency

if __name__ == "__main__":
    import doctest
    doctest.testmod()

