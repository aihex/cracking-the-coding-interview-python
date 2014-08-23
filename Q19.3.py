def trailing_zeros(n):
    res = 0
    for i in xrange(5, n+1, 5):
        while i != 0 and (i % 5) == 0:
            i /= 5
            res += 1
    return res


def f(n):
    res = 1
    for i in xrange(2, n+1):
        res *= i
    return res

if __name__ == '__main__':
    print trailing_zeros(5)
    print trailing_zeros(9)
    print trailing_zeros(10)
    print trailing_zeros(25)
    print f(25)
