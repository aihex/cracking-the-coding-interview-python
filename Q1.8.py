def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    if s2:
        return s2 in (s1 + s1)
    else:
        return s1 == s2 == ''

if __name__ == '__main__':
    print is_rotation('erwat', 'water')
    print is_rotation('erwat', 'watter')
    print is_rotation('erwat', 'w')
    print is_rotation('erwat', '')
    print is_rotation('', '')
