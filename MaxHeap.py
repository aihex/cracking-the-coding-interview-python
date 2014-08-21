import random
import time


class MaxHeap():
    def __init__(self, val=0):
        self.arr = [0, val]
        self.len = 2

    def insert(self, val):
        self.arr[self.len:] = [val]
        self.len += 1
        i = self.len - 1
        while i != 1:
            if self.arr[i] > self.arr[i/2]:
                self.arr[i], self.arr[i/2] = self.arr[i/2], self.arr[i]
                i /= 2
            else:
                break

    def pop(self):
        if self.len <= 1:
            return None
        res = self.arr[1]
        self.arr[1] = self.arr[self.len-1]
        self.len -= 1
        self.heapify(1)
        return res

    def heapify(self, i):
        largest = i
        if self.len > 2*i:
            # largest = max(self.arr[i], self.arr[2*i])
            largest = i if self.arr[i] >= self.arr[2*i] else 2*i
        if self.len > 2*i+1:
            # largest = max(largest, self.arr[2*i+1])
            largest = largest if self.arr[largest] >= self.arr[2*i+1] else 2*i+1
        if largest and largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(largest)

    @staticmethod
    def build_from_array(arr):
        arr_new = [0]
        arr_new[1:] = arr
        mp = MaxHeap()
        mp.arr = arr_new
        mp.len = len(arr_new)
        for i in xrange(mp.len - 1, 0, -1):
            mp.heapify(i)
        return mp

if __name__ == '__main__':
    s = time.time()
    mp = MaxHeap(1)
    for i in xrange(2, 1000000):
        mp.insert(i)
        # print mp.arr
    # print mp.arr[1:mp.len]
    # for i in xrange(9999, 0, -1):
    #     if mp.pop() != i:
    #         print 'wrong'
    #         break
    print time.time() - s
    # for i in xrange(99):
    #     print mp.pop()
    #     print mp.arr[1:mp.len]

    arr = [i for i in xrange(1, 1000000)]
    s = time.time()
    mp_1 = MaxHeap.build_from_array(arr)
    # print mp_1.arr[1:mp_1.len]
    # mp_1.pop()
    # print mp_1.arr[1:mp_1.len]
    # for i in xrange(9999, 0, -1):
    #     if mp_1.pop() != i:
    #         print 'wrong'
    #         break
    print time.time() - s
