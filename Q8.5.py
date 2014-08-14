def perm_paren(l, r, res, tmp):
    if r < l:
        return None
    if not l and not r:
        res.append(tmp)
    if l:
        perm_paren(l-1, r, res, tmp + '(')
    if r:
        perm_paren(l, r-1, res, tmp + ')')

if __name__ == '__main__':
    res = []
    print perm_paren(3, 3, res, '')
    print res
