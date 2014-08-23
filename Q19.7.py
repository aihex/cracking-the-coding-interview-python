def max_sub(arr):
    res = [arr[0] if arr[0] > 0 else 0]
    for i in xrange(1, len(arr)):
        if arr[i] + res[-1] > 0:
            res.append(arr[i] + res[-1])
        else:
            res.append(0)
    return max(res)

if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print max_sub(arr)
