def removeDuplicate(s):
    i = 0
    while i < len(s):
        j = i + 1
        while j < len(s):
            if s[i] == s[j]:
                s[j] = '\0'
            j += 1
        i += 1

    i = 0
    p = 0
    while i < len(s):
        if s[i] != '\0':
            s[p] = s[i]
            p += 1
        i += 1
    return ''.join(s[0:p])

if __name__ == '__main__':
    s = 'aaabcacbadc'
    print removeDuplicate(list(s))
