def tower(lst):
    lst = sorted(lst)
    print lst
    dp = [1 for i in xrange(len(lst))]
    for i in xrange(1, len(lst)):
        # print [(dp[j][0]+1, j) if lst[i][1] >= lst[j][1] else (dp[j][0], j) for j in xrange(i)]
        dp[i] = max([dp[j]+1 if lst[i][1] >= lst[j][1] else dp[j] for j in xrange(i)])
    print dp
    max_dp = max(dp)
    return max_dp


def lis_stack(lst):
    lst = sorted(lst)
    print lst
    stack = [lst[0][1]]
    for tup in lst[1:]:
        if tup[1] >= stack[-1]:
            stack.append(tup[-1])
        else:
            low = 0
            high = len(stack) - 1
            while low > high:
                mid = (low + high) >> 1
                if stack[mid] == tup[1]:
                    break
                elif stack[mid] > tup[1]:
                    high = mid - 1
                else:
                    low = mid + 1
            stack[low] = tup[1]
    return len(stack)


if __name__ == '__main__':
    lst = [(65, 100), (70, 150), (56, 100), (75, 100), (60, 95), (68, 110)]
    print tower(lst)
    print lis_stack(lst)
