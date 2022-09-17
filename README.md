# python-primes
primes prime-factorization pseudo-random-numbers<br>
Usage: ./driver.py n<br>
example run<br>
<pre>
./driver.py 20
n = 20
Factorizing 20 13-bit pseudo-random nos.
7072: [2, 2, 2, 2, 2, 13, 17]
45: [3, 3, 5]
7201: [19, 379]
5398: [2, 2699]
4109: [7, 587]
7894: [2, 3947]
6534: [2, 3, 3, 3, 11, 11]
3690: [2, 3, 3, 5, 41]
730: [2, 5, 73]
322: [2, 7, 23]
1107: [3, 3, 3, 41]
219: [3, 73]
3373: [3373]
7704: [2, 2, 2, 3, 3, 107]
2523: [3, 29, 29]
1831: [1831]
673: [673]
1576: [2, 2, 2, 197]
6283: [61, 103]
1021: [1021]
Factorizing 20 17-bit pseudo-random nos.
48245: [5, 9649]
40102: [2, 20051]
76628: [2, 2, 19157]
65444: [2, 2, 16361]
86380: [2, 2, 5, 7, 617]
114318: [2, 3, 3, 3, 29, 73]
128586: [2, 3, 29, 739]
88376: [2, 2, 2, 11047]
17013: [3, 53, 107]
120881: [109, 1109]
38014: [2, 83, 229]
47347: [113, 419]
18344: [2, 2, 2, 2293]
23227: [23227]
14555: [5, 41, 71]
44102: [2, 22051]
12699: [3, 3, 17, 83]
3511: [3511]
58213: [23, 2531]
78446: [2, 61, 643]
Factorizing 20 31-bit pseudo-random nos.
2047185442: [2, 1023592721]
1080970430: [2, 5, 79, 113, 12109]
2113455371: [26203, 80657]
246079159: [53, 4643003]
755032532: [2, 2, 1319, 143107]
1230378935: [5, 4691, 52457]
813829953: [3, 23, 11794637]
467306692: [2, 2, 116826673]
193101444: [2, 2, 3, 3, 2143, 2503]
1120775344: [2, 2, 2, 2, 13, 19, 41, 6917]
1538595000: [2, 2, 2, 3, 3, 3, 3, 5, 5, 5, 5, 29, 131]
944797152: [2, 2, 2, 2, 2, 3, 13, 131, 5779]
193112853: [3, 23, 2798737]
1671499183: [67, 577, 43237]
1828961156: [2, 2, 11, 2699, 15401]
583749459: [3, 3, 3947, 16433]
1037203102: [2, 13, 503, 79309]
397190484: [2, 2, 3, 3, 43, 379, 677]
47852748: [2, 2, 3, 3, 3, 563, 787]
1355078183: [277, 4891979]
Computing primes using naive simple sieve.
[2, 3, 5, 7, 11, 13, 17, 19]
Computing primes using set differences simple sieve.
[2, 3, 5, 7, 11, 13, 17, 19]
Computing primes using segmented sieve.
[2, 3, 5, 7, 11, 13, 17, 19]
Computing primes using primality predicate filter sieve.
[2, 3, 5, 7, 11, 13, 17, 19]
Counting primes using primality predicate.
Π(20) = 8
</pre>
<br>
<pre>
./test.py 10000
n = 10000
Computing primes using primality predicate filter.
Elapsed time: 0.000 seconds
Π(10000) = 1229

Computing primes using simple sieve.
Elapsed time: 0.546 seconds
Π(10000) = 1229

Computing primes using simple sieve (set differences).
Elapsed time: 0.008 seconds
Π(10000) = 1229

Computing primes using segmented sieve.
Elapsed time: 0.000 seconds
Π(10000) = 1229

Counting primes using primality predicate test.
Elapsed time: 0.000 seconds
Π(10000) = 1229
</pre>
