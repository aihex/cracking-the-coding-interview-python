import random
import time


class MaxHeap():
    def __init__(self):
        self.arr = []
        self.len = 0

    def insert(self, val):
        self.arr.append(val)
        self.len += 1
        i = self.len - 1
        while i != 0:
            if self.arr[i] > self.arr[(i-1) >> 1]:
                self.arr[i], self.arr[(i-1) >> 2] = self.arr[(i-1) >> 2], self.arr[i]
                i = (i-1) >> 2
            else:
                break

    def pop(self):
        if not self.len:
            return None
        res = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.len -= 1
        self.heapify(0)
        return res

    def heapify(self, i):
        large_idx = i
        if (i << 1) + 1 < self.len:  # has left child
            large_idx = i if self.arr[i] >= self.arr[(i << 1) + 1] else (i << 1) + 1
        if (i << 1) + 2 < self.len + 1:  # has right child
            large_idx = large_idx if self.arr[large_idx] >= self.arr[(i << 1) + 2] else (i << 1) + 2
        if large_idx and large_idx != i:
            self.arr[i], self.arr[large_idx] = self.arr[large_idx], self.arr[i]
            self.heapify(large_idx)

    @staticmethod
    def build_from_array(arr):
        mp = MaxHeap()
        mp.arr = arr[:]
        mp.len = len(mp.arr)
        for i in xrange(mp.len >> 1, -1, -1):
            mp.heapify(i)
        return mp

if __name__ == '__main__':
    s = time.time()
    mp = MaxHeap()
    for i in xrange(1, 10):
        mp.insert(i)
        print mp.arr
    # print mp.arr[1:mp.len]
    # for i in xrange(9999, 0, -1):
    #     if mp.pop() != i:
    #         print 'wrong'
    #         break
    print time.time() - s
    # for i in xrange(99):
    #     print mp.pop()
    #     print mp.arr[1:mp.len]

    arr = [i for i in xrange(1, 10)]
    s = time.time()
    mp_1 = MaxHeap.build_from_array(arr)
    # print mp_1.arr
    # mp_1.pop()
    # print mp_1.arr[1:mp_1.len]
    # for i in xrange(9999, 0, -1):
    #     if mp_1.pop() != i:
    #         print 'wrong'
    #         break
    print time.time() - s
