import os
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from statistics.basic import Statistics
from optparse import OptionParser, OptionValueError


if __name__ == "__main__":
    usage = "usage: %prog [options] keyword"
    parser = OptionParser(usage)

    parser.add_option(
        "-s", "--samples",
        type="int",
        dest="samples",
        default=1000,
        help="number of samples"
    )
    parser.add_option(
        "-e", "--executions",
        type="int",
        dest="executions",
        default=1000,
        help="number of executions"
    )
    parser.add_option(
        "-m", "--mean",
        type="float",
        dest="mean",
        default=1.0,
        help="mean"
    )
    parser.add_option(
        "-n", "--name",
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
    arr = [x for x in xrange(options.executions)]
    ax.plot(arr)
    file_name = "{}.{}".format(options.file_name, options.file_type)
    plt.savefig(file_name, format=options.file_type)
    fig.savefig(options.file_name)
