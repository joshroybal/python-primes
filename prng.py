# global state variable
seed = 0

def reset():
    global seed
    seed = 0

def randomize(n):
    global seed
    seed = n
    if seed % 2 == 0:
        seed += 1

# n is no. of significant bits
def prng(n):
    global seed
    if n == 8:
        seed = (125*seed+123)%(2**n)
    elif n == 13:
        seed = (8169*seed)%(2**n-1)
    elif n == 16:
        seed = (16385*seed+12345)%(2**n)
    elif n == 17:
        seed = (32719*seed)%(2**n-1)
    elif n == 31:
        seed = (48271*seed)%(2**n-1)
    elif n == 32:
        seed = (1103515245*seed+123456789)%(2**n)
    elif n == 48:
        seed = (44485709377909*seed+11863279)%(2**n)
    elif n == 61:
        seed = (437799614237992725*seed)%(2**n-1)
    else:
        seed = (2862933555777941757*seed+3037000493)%(2**n);
    return seed
