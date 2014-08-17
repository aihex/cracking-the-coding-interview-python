def give_changes(leftover, candidates, start, res, stack):
    if leftover == 0:
        res.append(list(stack))
    elif leftover > 0:
        for i in xrange(start, len(candidates)):
            stack.append(candidates[i])
            give_changes(leftover-candidates[i], candidates, i, res, stack)
            stack.pop()

if __name__ == '__main__':
    res = []
    give_changes(100, [1, 5, 10, 25], 0, res, [])
    print res
    print '\n'.join([' '.join(str(item) for item in array) for array in res])
