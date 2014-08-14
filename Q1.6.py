def transpose(matrix):
    N = len(matrix)
    for i in xrange(N-1):
        for j in xrange(i+1, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in xrange(N/2):
        matrix[i], matrix[N-1-i] = matrix[N-1-i], matrix[i]
    return matrix

if __name__ == '__main__':
    matrix = [[j for j in xrange(i*4, (i+1)*4)] for i in xrange(4)]
    print '\n'.join([str(m) for m in matrix])
    transpose(matrix)
    print 
    print '\n'.join([str(m) for m in matrix])
