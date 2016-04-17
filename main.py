import os
import sys
from statistics.basic import Statistics
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

    options, args = parser.parse_args()
    if options.data_file:
        with open(options.data_file,"r") as f:
            data = map(int, f.read().split())
    else:
        data = map(int, args)
    s = Statistics(data, bin_width=options.bin_width, bins=options.bins)
    F = 0
    P = 0
    for i, v in sorted(s.frequency.items()):
        f = len(v)
        F += f
        p = f / s.length
        P += p
        print i, f, F, p, P, v
