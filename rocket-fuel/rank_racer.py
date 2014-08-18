def rank_racer(file_name):
    f = open(file_name)
    lines = f.readlines()
    info_array = []
    for line in lines[1:]:
        sps = line.rstrip().split()
        info_array.append([int(sps[1]), int(sps[2]), int(sps[0]), 0])
    f.close()
    info_array.sort()  # sort based on starting time
    print info_array
    merge_sort(info_array, 0, len(info_array)-1)
    res = []
    print info_array
    for line in info_array:
        res.append([line[3], line[2]])
    res.sort()  # sorted based on score and then id
    res = [[line[1], line[0]]for line in res]
    return res


def merge_sort(array, start, end):
    if start >= end:
        return None
    else:
        mid = (start + end) >> 1
        merge_sort(array, start, mid)
        merge_sort(array, mid + 1, end)
        i = start
        j = mid + 1
        tmp_array = []
        while i <= mid and j <= end:
            if array[i][1] < array[j][1]:  # the earlier starting one ends eailier
                tmp_array.append(array[i])
                i += 1
            else:
                array[i][3] += 1
                tmp_array.append(array[j])  # the earlier starting one ends later
                j += 1
        while i <= mid:
            array[i][3] += 1
            tmp_array.append(array[i])  # all left ealier starting ones should +1
            i += 1
        while j <= end:
            tmp_array.append(array[j])
            j += 1
        array[start:end+1] = tmp_array


if __name__ == '__main__':
    res = rank_racer('rank.txt')
    print '\n'.join(' '.join(str(item) for item in array) for array in res)
