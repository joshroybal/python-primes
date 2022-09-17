#!/usr/bin/env python

import sys, time
import prng, primes

def message(t, t0):
    string = 'Elapsed time: {:.3f} seconds'.format(t - t0)
    print(string)

def main(n):
    print('n =', n)

    print('Computing primes using primality predicate filter.')
    t0 = time.time()
    result = len(primes.primes(n))
    message(time.time(), t0)
    string = '\u03A0(' + str(n) + ') = ' + str(result)
    print(string)
    print()

    # just too inefficient most of the time
    # uncomment if you want to see how inefficient
    if n <= 10000:
        print('Computing primes using simple sieve.')
        t0 = time.time()
        result = len(primes.sieve(n))
        message(time.time(), t0)
        string = '\u03A0(' + str(n) + ') = ' + str(result)
        print(string)
        print()

    print('Computing primes using simple sieve (set differences).')
    t0 = time.time()
    result = len(primes.simple_sieve(n))
    message(time.time(), t0)
    string = '\u03A0(' + str(n) + ') = ' + str(result)
    print(string)
    print()

    print('Computing primes using segmented sieve.')
    t0 = time.time()
    result = len(primes.segmented_sieve(n))
    message(time.time(), t0)
    string = '\u03A0(' + str(n) + ') = ' + str(result)
    print(string)
    print()

    print('Counting primes using primality predicate test.')
    t0 = time.time()
    result = primes.count_primes(n)
    message(time.time(), t0)
    string = '\u03A0(' + str(n) + ') = ' + str(result)
    print(string)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: %s n\n' % sys.argv[0])
        sys.exit(1)
    try:
        main(int(sys.argv[1]))
    except Exception as error:
        sys.stderr.write('%s\n' % error)
        sys.exit(1)
