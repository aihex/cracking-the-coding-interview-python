import random


def rand_perm(obj):
    if type(obj) is str:
        arr = list(obj)
    else:
        arr = obj
    for i in xrange(len(arr)-1):
        r = random.randint(i, len(arr)-1)
        arr[i], arr[r] = arr[r], arr[i]


if __name__ == '__main__':
    arr = [i for i in xrange(1, 100)]
    rand_perm(arr)
    print arr
