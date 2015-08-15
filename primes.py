#!/usr/bin/python

import sys
import time
import argparse
start = time.time()
primes = []


def amiprime(check, verbose, f):
    before = time.time()
    for prime in primes:
        if check%prime == 0:
            return
    now = time.time()
    primes.append(check)
    difference = now - before
    it = '%s took %s seconds to calculate' % (check, difference)
    f.write(it + '\n')
    if verbose:
        print it
    if difference > 0.5:
        print 'prime %s' % it


def myclose(primes, outfile, f):
    elapsed = time.time() - start
    time_to_calculate = '\ntook %s seconds to calculate' % elapsed
    if elapsed > 60:
        minutes = elapsed / 60
        time_to_calculate += '\nwhich is %s minutes' % minutes
        if minutes > 60:
            hours = minutes / 60
            time_to_calculate += '\nand %s hours' % hours
            if hours > 24:
                days = hours / 24
                time_to_calculate += '\nand %s days' % days
                if days > 7:
                    weeks = days / 7
                    time_to_calculate += '\nand %s weeks' % weeks
                    if weeks > 52:
                        years = weeks / 52
                        time_to_calculate += '\nand %s years' % years
    time_to_calculate += '\n'
    if args.verbose:
        print time_to_calculate
    f.write(time_to_calculate)
    f.close()
    sys.exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--countto', default=100000, action='store',
                        help='number to count to (default: 100000)')
    parser.add_argument('--outfile', default='./primes_out.txt',
                        help='output file (default: ./primes_out.txt)')
    parser.add_argument('--verbose', default=False, action='store_true',
                        help='print primes as they are discovered')
    args = parser.parse_args()
    f = open(args.outfile, 'w')
    # we start calculations at 3, because i'm too lazy to bother to do a
    # check to be sure that we are not dividing by 1 and because we are
    # inherently skipping everything which is divisible by 2 to increase
    # speed, so we need to include 1 and 2 in the output.
    f.write('1\n2\n')
    if args.verbose:
        print '1\n2'
    checknum = 3
    try:
        while checknum < int(args.countto):
            amiprime(checknum, args.verbose, f)
            checknum += 2
        myclose(primes, args, f)
    except KeyboardInterrupt:
        myclose(primes, args, f)
