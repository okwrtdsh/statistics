import os
import sys
from statistics.basic import Statistics
from statistics.chisquare import chisquare
from optparse import OptionParser, OptionValueError


if __name__ == "__main__":
    usage = "usage: %prog [options] keyword"
    parser = OptionParser(usage)

    parser.add_option(
        "-f", "--file",
        action="store",
        type="string",
        dest="data_file",
        help="data file"
    )
    parser.add_option(
        "-b", "--bins",
        type="int",
        dest="bins",
        default=None,
        help="bins"
    )
    parser.add_option(
        "-w", "--bin_width",
        type="int",
        dest="bin_width",
        default=None,
        help="bin width"
    )
    parser.add_option(
        "-s", "--significance_level",
        type="float",
        dest="significance_level",
        default=0.05,
        help="significance level"
    )

    options, args = parser.parse_args()
    if options.data_file:
        with open(options.data_file,"r") as f:
            data = map(int, f.read().split())
    else:
        data = map(int, args)
    s = Statistics(
        data,
        bin_width=options.bin_width,
        bins=options.bins,
        significance_level=options.significance_level
    )
    for c in s.classes:
        print "{:<5}\t{:<3}\t{:<15}\t{:<15}\t{:<15}\t{:<17}\t{:<15}".format(
            c,
            s.frequencies[c],
            s.proportions[c],
            s.zscores[c],
            s.cumulative_ratios[c],
            s.class_ratios[c],
            s.expectations[c]
        )
    result = s.fit_test()
    print(s.chisquare)
    print(s.freedom)
    print(s.critical_region)
    print(result)



