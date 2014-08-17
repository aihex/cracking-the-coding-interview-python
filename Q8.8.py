def queen_problem(matrix):
    queen_problem_rec(matrix, 0)


def queen_problem_rec(matrix, row):
    if row > len(matrix):
        print '\n'.join([' '.join([str(s) for s in array]) for array in matrix])
    for i in xrange(len(matrix)):
        if is_safe(matrix, row, i):
            matrix[row][i] = 'Q'
            queen_problem_rec(matrix, row+1)
            matrix[row][i] = '*'


def is_safe(matrix, row, i):
    pass

if __name__ == '__main__':
    N = 8
    matrix = [['*' for c in xrange(N)] for r in xrange(N)]
    print '\n'.join([' '.join(array) for array in matrix])
