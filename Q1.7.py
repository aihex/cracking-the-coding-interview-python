def set_zeros(matrix):
    zero_first_row = not all(matrix[0])
    zero_first_col = not all([matrix[i][0] for i in xrange(len(matrix))])
    for i in xrange(1, len(matrix)):
        for j in xrange(1, len(matrix)):
            if not matrix[i][j]:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in xrange(1, len(matrix)):
        if not matrix[0][i]:
            for j in xrange(1, len(matrix)):
                matrix[j][i] = 0
    for i in xrange(1, len(matrix)):
        if not matrix[i][0]:
            matrix[i][1:] = [0 for j in xrange(1, len(matrix))]
    if zero_first_row:
        matrix[0][:] = [0 for i in xrange(len(matrix))]
    if zero_first_col:
        for i in xrange(len(matrix)):
            matrix[i][0] = 0

if __name__ == '__main__':
    N = 5
    matrix = [[1 for j in xrange(N)] for i in xrange(N)]
    print '\n'.join([' '.join([str(j) for j in array]) for array in matrix])
    print
    matrix[0][0] = 0
    matrix[2][2] = 0
    set_zeros(matrix)
    print '\n'.join([' '.join([str(j) for j in array]) for array in matrix])
    print
