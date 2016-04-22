# -*- coding: utf-8 -*-
import math
from .normal import normal
from .chisquare import chisquare


class Statistics(object):
    _total = None
    _length = None
    _mean = None
    _variance = None
    _stdev = None
    _classes = None
    _frequencies = None
    _proportions = None
    _zscores = None
    _cumulative_ratios = None
    _class_ratios = None
    _expectations = None
    _chisquare = None
    _fit_test = None
    freedom = None
    critical_region = None

    def __init__(self, data, bins=None, bin_width=None, significance_level=None):
        """
        >>> Statistics([1, 2, 3, 4, 5]).data
        [1.0, 2.0, 3.0, 4.0, 5.0]
        """
        self.data = map(float, sorted(data))
        self._bins = bins
        self._bin_width = bin_width
        self.significance_level = significance_level

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
            self._bins = int(
                math.ceil(1 + (math.log(self.length, 10) / math.log(2, 10))))
        return self._bins

    @property
    def bin_width(self):
        """
        階級幅
        """
        if self._bin_width is None:
            self._bin_width = int(
                math.ceil((self.data[-1] - self.data[0]) / float(self.bins)))
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
                    result.append(result[i - 1] + self.bin_width)
            self._classes = result
        return self._classes

    @property
    def frequencies(self):
        """
        度数
        """
        if self._frequencies is None:
            result = {}
            i = 0
            for c in self.classes:
                cnt = 0
                while i < self.length and self.data[i] < c:
                    i += 1
                    cnt += 1
                result[c] = cnt
            self._frequencies = result
        return self._frequencies

    @property
    def proportions(self):
        """
        比率
        """
        if self._proportions is None:
            result = {}
            frequencies = self.frequencies
            for c in self.classes:
                result[c] = frequencies[c] / self.length
            self._proportions = result
        return self._proportions

    @property
    def zscores(self):
        """
        Z score
        """
        if self._zscores is None:
            result = {}
            for c in self.classes:
                result[c] = (c - self.mean) / self.stdev
            self._zscores = result
        return self._zscores

    @property
    def cumulative_ratios(self):
        """
        累積比率
        """
        if self._cumulative_ratios is None:
            result = {}
            zscores = self.zscores
            for c in self.classes:
                result[c] = normal(zscores[c])
            self._cumulative_ratios = result
        return self._cumulative_ratios

    @property
    def class_ratios(self):
        """
        階級比率
        """
        if self._class_ratios is None:
            result = {}
            cumulatives = self.cumulative_ratios
            cs = self.classes
            s = 0
            for i in range(len(cs)):
                result[cs[i]] = cumulatives[cs[i]]
                if i > 0:
                    result[cs[i]] -= cumulatives[cs[i - 1]]
                s += result[cs[i]]
            for c in cs:
                result[c] *= 1.0 / s
            self._class_ratios = result
        return self._class_ratios

    @property
    def expectations(self):
        """
        期待度数
        """
        if self._expectations is None:
            result = {}
            crs = self.class_ratios
            for c in self.classes:
                result[c] = self.length * crs[c]
            self._expectations = result
        return self._expectations

    @property
    def chisquare(self):
        if self._chisquare is None:
            es = self.expectations
            fs = self.frequencies
            cs = self.classes
            x, f, e, cnt = 0.0, 0.0, 0.0, 0.0
            for c in self.classes:
                if f + fs[c] < 5.0:
                    f += fs[c]
                    e += es[c]
                    continue
                x += (f - e) ** 2.0 / e
                f = fs[c]
                e = es[c]
                cnt += 1.0
            else:
                x += (f - e) ** 2.0 / e
                cnt += 1.0
            self._chisquare = x
            self.freedom = cnt - 2 - 1
        return self._chisquare

    def fit_test(self):
        if self._fit_test is None:
            x = self.chisquare
            self.critical_region = chisquare(self.freedom, self.significance_level)
            if x < self.critical_region:
                result = "accept"
            else:
                result = "reject"
            self._fit_test = result
        return self._fit_test


if __name__ == "__main__":
    import doctest
    doctest.testmod()

