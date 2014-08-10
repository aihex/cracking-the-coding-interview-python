def subsets(lst, start, res):
    if start == len(lst):
        res.append([])
        return
    subsets(lst, start+1, res)
    res.extend([item + [lst[start]] for item in list(res)])

if __name__ == '__main__':
    res = []
    subsets(list(xrange(3)), 0, res)
    print res
