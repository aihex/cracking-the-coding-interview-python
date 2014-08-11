def perm(lst, visited, res, tmp):
    if len(tmp) == len(lst):
        res.append(list(tmp))
    for i in xrange(len(lst)):
        if not visited[i]:
            tmp.append(lst[i])
            visited[i] = True
            perm(lst, visited, res, tmp)
            visited[i] = False
            tmp.pop()


if __name__ == '__main__':
    res = []
    tmp = []
    lst = [i for i in xrange(3)]
    visited = [False for i in xrange(len(lst))]
    perm(lst, visited, res, tmp)
    print res
