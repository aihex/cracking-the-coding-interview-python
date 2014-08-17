def find_one_missing(lst):
    list_tmp = list(xrange(1, len(lst)+2))
    list_tmp.extend(lst)
    return reduce(lambda x, y: x ^ y, list_tmp)


def find_two_missing(lst):
    list_tmp = list(xrange(1, len(lst)+3))
    list_tmp.extend(lst)
    tmp_xor = reduce(lambda x, y: x ^ y, list_tmp)
    i = 0
    while not (tmp_xor & (1 << i)):
        i += 1
    list_a = [num for num in lst if num & (1 << i)]
    list_b = [num for num in lst if not (num & (1 << i))]
    list_a_all = [num for num in list(xrange(1, len(lst)+3)) if num & (1 << i)]
    list_a_all.extend(list_a)
    list_b_all = [num for num in list(xrange(1, len(lst)+3)) if not (num & (1 << i))]
    list_b_all.extend(list_b)
    return reduce(lambda x, y: x ^ y, list_a_all), reduce(lambda x, y: x ^ y, list_b_all)


if __name__ == '__main__':
    lst = list(xrange(1, 20))
    lst.pop(10)
    print lst
    print find_one_missing(lst)
    lst.pop(7)
    print lst
    print find_two_missing(lst)
