import sys
import random

def stack_sort(stack):
    stack_res = []
    stack_tmp = []
    while stack:
        min_tmp = sys.maxint
        while stack:
            tmp = stack.pop()
            if tmp < min_tmp:
                min_tmp = tmp
            stack_tmp.append(tmp)
        while stack_tmp:
            tmp = stack_tmp.pop()
            if tmp != min_tmp:
                stack.append(tmp)
            else:
                stack_res.append(tmp)
    return stack_res

if __name__ == '__main__':
    stack = [random.randint(0, 20) for i in xrange(20)]
    print stack
    print stack_sort(stack)
