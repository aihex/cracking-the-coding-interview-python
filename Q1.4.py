def is_anagram(s, t):
    req = {}
    for i in s:
        if i not in req.keys():
            req[i] = 1
        else:
            req[i] += 1

    for i in t:
        if i not in t:
            return False
        else:
            req[i] -= 1

    for v in req.values():
        if v != 0:
            return False
    return True


if __name__ == '__main__':
    print is_anagram('abced', 'decbaa')
