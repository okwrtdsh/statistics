# -*- coding: utf-8 -*-
import math
from normal import normal
from chisquare import chisquare


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
        >>> Statistics([1, 2, 3, 4, 5], bins=10).bins
        10
        >>> Statistics([1, 2, 3, 4, 5], bin_width=3).bin_width
        3
        >>> Statistics([1, 2, 3, 4, 5], significance_level=0.05).significance_level
        0.05
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
        >>> Statistics(range(100)).bins
        8
        """
        if self._bins is None:
            self._bins = int(
                math.ceil(1 + (math.log(self.length, 10) / math.log(2, 10))))
        return self._bins

    @property
    def bin_width(self):
        """
        階級幅
        >>> Statistics(range(100)).bin_width
        13
        """
        if self._bin_width is None:
            self._bin_width = int(
                math.ceil((self.data[-1] - self.data[0]) / float(self.bins)))
        return self._bin_width

    @property
    def classes(self):
        """
        階級の上限値のリスト
        >>> Statistics(range(100)).classes
        [0.5, 13.5, 26.5, 39.5, 52.5, 65.5, 78.5, 91.5, 104.5]
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
        >>> Statistics(range(100)).frequencies
        {0.5: 1, 13.5: 13, 39.5: 13, 78.5: 13, 52.5: 13, 91.5: 13, 26.5: 13, 104.5: 8, 65.5: 13}
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
        >>> Statistics(range(100)).proportions
        {0.5: 0.01, 13.5: 0.13, 39.5: 0.13, 78.5: 0.13, 52.5: 0.13, 91.5: 0.13, 26.5: 0.13, 104.5: 0.08, 65.5: 0.13}
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
        >>> Statistics(range(100)).zscores
        {0.5: -1.6974946682728878, 13.5: -1.247138939955591, 39.5: -0.3464274833209975, 78.5: 1.0046397016308928, 52.5: 0.10392824499629925, 91.5: 1.4549954299481895, 26.5: -0.7967832116382942, 104.5: 1.9053511582654863, 65.5: 0.554283973313596}
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
        >>> Statistics(range(100)).cumulative_ratios
        {0.5: 0.044801589515958584, 13.5: 0.10617327880370742, 39.5: 0.36451073683111224, 78.5: 0.8424648134080693, 52.5: 0.5413868538950893, 91.5: 0.9271647362994231, 26.5: 0.21278847359990977, 104.5: 0.9716327798333377, 65.5: 0.7103077415494481}
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
        >>> Statistics(range(100)).class_ratios
        {0.5: 0.04610959041917391, 13.5: 0.06316346109512258, 39.5: 0.1561518573480272, 78.5: 0.13601545213541466, 52.5: 0.18204008832875762, 91.5: 0.08717277211034621, 26.5: 0.1097278694266468, 104.5: 0.04576630642447259, 65.5: 0.17385260271203842}
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
        >>> Statistics(range(100)).expectations
        {0.5: 4.610959041917391, 13.5: 6.316346109512258, 39.5: 15.61518573480272, 78.5: 13.601545213541467, 52.5: 18.20400883287576, 91.5: 8.717277211034622, 26.5: 10.97278694266468, 104.5: 4.576630642447259, 65.5: 17.385260271203844}
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
        """
        カイ二乗値
        >>> Statistics(range(100)).chisquare
        17.99786751906374
        """
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
        """
        適合度検定
        >>> Statistics(range(100), significance_level=0.05).fit_test()
        'reject'
        """
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

