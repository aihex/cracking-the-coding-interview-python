def print_binary(num_str):
    '''
    num = a2 * 2^2 + a1 * 2^1 + a0 * 2^0 + a-1 * 2^-1 + a-2 * 2^-2
    a2 = num / 2^2
    a1 = num / 2^1
    a0 = num / 2^0
    a-1 = num / 2^-1 = num * 2^1
    a-2 = num / 2^-2 = num * 2^2
    '''

    pos = num_str.index('.')
    num_1 = int(num_str[0:pos])
    num_2 = float('0' + num_str[pos:])

    print num_1, num_2
    str_1 = ''
    while num_1 > 0:
        if num_1 & 1:
            str_1 += '1'
        else:
            str_1 += '0'
        num_1 >>= 1

    str_2 = ''
    while num_2 > 0:
        num_2 *= 2
        if num_2 >= 1:
            str_2 += '1'
            num_2 -= 1
        else:
            str_2 += '0'

    return str_1 + '.' + str_2


if __name__ == '__main__':
    print print_binary('3.3')
