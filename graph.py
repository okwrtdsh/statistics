import os
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from statistics.basic import Statistics
from optparse import OptionParser, OptionValueError
from statistics.normal_random import normal_random


if __name__ == "__main__":
    usage = "usage: %prog [options] keyword"
    parser = OptionParser(usage)

    parser.add_option(
        "-n", "--number",
        type="int",
        dest="number",
        default=1000,
        help="number of samples"
    )
    parser.add_option(
        "-a", "--avarage",
        type="int",
        dest="avarage",
        default=150,
        help="avarage"
    )
    parser.add_option(
        "-s", "--sigma",
        type="float",
        dest="sigma",
        default=10.0,
        help="sigma"
    )
    parser.add_option(
        "-e", "--executions",
        type="int",
        dest="executions",
        default=1000,
        help="number of executions"
    )
    parser.add_option(
        "-f", "--file_name",
        action="store",
        type="string",
        dest="file_name",
        default="output",
        help="output file name"
    )
    parser.add_option(
        "-t", "--type",
        action="store",
        type="string",
        dest="file_type",
        default="png",
        help="output file type"
    )

    options, args = parser.parse_args()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    import math
    import numpy as np
    def pdf(x, n):
        return x**(n/2.0 - 1.0) * math.exp(-x/2.0) / (2.0**(n/2.0)*math.gamma(n/2.0))
    C = 250
    for n in xrange(1, 11):
        x=np.linspace( 0., 25., C)[1:]
        y = [pdf(i, n) for i in x]
        ax.plot(x, y, label="n=%s" % n)

    l = []
    for _ in xrange(options.executions):
        l.append(Statistics(normal_random(
            options.number,
            mu=options.avarage,
            sigma=options.sigma
        )).chisquare)
    ax.hist(l, bins=100, normed=True, label="random data")

    ax.legend()

    file_name = "{}.{}".format(options.file_name, options.file_type)
    plt.xlim(0, 25)
    plt.ylim(0, 0.3)
    plt.savefig(file_name, format=options.file_type)
    fig.savefig(options.file_name)

