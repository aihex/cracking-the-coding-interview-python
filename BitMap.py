import sys


class BitMap():
    int_size = 8*sys.getsizeof(0)

    def __init__(self, size=0):
        self.array = [0 for i in xrange(size / BitMap.int_size + 1)]

    def get(self, pos):
        offset1 = pos / BitMap.int_size
        offset2 = pos % BitMap.int_size
        return self.array[offset1] & (1 << offset2)

    def set(self, pos):
        offset1 = pos / BitMap.int_size
        offset2 = pos % BitMap.int_size
        self.array[offset1] |= 1 << offset2


if __name__ == '__main__':
    bm = BitMap(10)
    print bm.int_size
    print bm.get(1)
    bm.set(2)
    print bm.get(2)
    bm.set(0)
    print bm.array[0]
