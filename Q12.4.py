import random
from BitMap import BitMap


def dedup(array):
    N = 32000
    bm = BitMap(N)
    for i in array:
        if bm.get(i-1):
            print i,
        else:
            bm.set(i-1)


if __name__ == '__main__':
    N = 32000
    array = [random.randint(1, N) for i in xrange(N)]
    print array
    dedup(array)
