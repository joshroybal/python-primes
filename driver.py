#!/usr/bin/env python

import sys, time
import primes, prng

def report(nobits, n):
    print(str(nobits)+'-bit pseudo-random nos.')
    prng.randomize(int(time.time())%(2**nobits))
    for i in range(n):
        z = prng.prng(nobits)
        print(str(z)+':', primes.factorize(z))

def main(n):
    print('n =', n)
    #report(8, n)
    report(13, n)
    report(16, n)
    report(17, n)
    report(31, n)
    #report(32, n)
    #report(48, n)
    # even on the quad core these were too slow
    #report(61, n)
    #report(64, n)
    print(primes.sieve(n))
    print(primes.segmented_sieve(n))
    print(primes.primes(n))
    print(primes.count_primes(n))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: %s n\n' % sys.argv[0])
        sys.exit(1)
    try:
        main(int(sys.argv[1]))
    except Exception as error:
        sys.stderr.write('%s\n' % error)
        sys.exit(1)
