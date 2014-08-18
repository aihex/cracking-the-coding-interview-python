def match(l_paren, r_paren, l_brack, r_brack, l_brace, r_brace, res, tmp_str):
    if r_paren < l_paren or r_brack < l_brack or r_brace < l_brace:
        return None
    if l_paren == r_paren == l_brack == r_brack == l_brace == r_brace == 0:
        res.append(tmp_str)
    if l_paren and l_brack == r_brack and l_brace == r_brace:
        match(l_paren-1, r_paren, l_brack, r_brack, l_brace, r_brace, res, tmp_str + '(')
    if r_paren and l_brack == r_brack and l_brace == r_brace:
        match(l_paren, r_paren-1, l_brack, r_brack, l_brace, r_brace, res, tmp_str + ')')
    if l_brack and l_paren == r_paren and l_brace == r_brace:
        match(l_paren, r_paren, l_brack-1, r_brack, l_brace, r_brace, res, tmp_str + '[')
    if r_brack and l_paren == r_paren and l_brace == r_brace:
        match(l_paren, r_paren, l_brack, r_brack-1, l_brace, r_brace, res, tmp_str + ']')
    if l_brace and l_paren == r_paren and l_brack == r_brack:
        match(l_paren, r_paren, l_brack, r_brack, l_brace-1, r_brace, res, tmp_str + '{')
    if r_brace and l_paren == r_paren and l_brack == r_brack:
        match(l_paren, r_paren, l_brack, r_brack, l_brace, r_brace-1, res, tmp_str + '}')

if __name__ == '__main__':
    res = []
    match(4, 4, 4, 4, 4, 4, res, '')
    print len(res)
    print '\n'.join(res)
