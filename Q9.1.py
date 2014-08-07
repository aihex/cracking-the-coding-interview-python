def merge(a, b, k):
    i = k + len(b) - 1
    j = len(b) - 1
    k -= 1
    while k >= 0 and j >= 0:
        if a[k] > b[j]:
            a[i] = a[k]
            k -= 1
        else:
            a[i] = b[j]
            j -= 1

        i -= 1

    if k == -1:
        a[0:i+1] = b[0:j+1]

    return a

if __name__ == '__main__':
    a = [1, 2, 2, 4, 5, 6, 6]
    b = [1, 1, 3, 4, 9]
    k = len(a)
    a.extend([0 for i in xrange(len(b))])
    print a
    print merge(a, b, k)
