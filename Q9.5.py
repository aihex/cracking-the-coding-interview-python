def binary_search(array, tar):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) >> 1
        if array[mid] == tar:
            return mid
        move_mid = mid
        while move_mid >= low and not array[move_mid]:
            move_mid -= 1
        if move_mid < low:
            low = mid + 1
            continue
        if array[move_mid] == tar:
            return move_mid
        elif array[move_mid] > tar:
            high = move_mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    array = ['', 'a', '', '', 'c', '', '']
    print binary_search(array, '')
    print binary_search(array, 'a')
    print binary_search(array, 'b')
    print binary_search(array, 'c')
