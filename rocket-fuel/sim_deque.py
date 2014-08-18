def sim_deque(pop_seq):
    pop_seq = list(reversed(pop_seq))
    res = [1]
    idx_seq = [0 for i in xrange(len(pop_seq)+1)]
    i = 1
    for item in pop_seq:
        idx_seq[item] = i
        i += 1
    count = 1
    ins_seq = [1]
    while pop_seq:
        while pop_seq and pop_seq[-1] <= count:  # pop out what can be popped
            if ins_seq[-1] == pop_seq[-1]:
                res.append(3)
                pop_seq.pop()
                ins_seq.pop()
            else:
                return None
        if not pop_seq:  # maybe program has finished
            break
        count += 1
        if not ins_seq or idx_seq[count] > idx_seq[ins_seq[-1]]:
            res.append(1)  # when new idx is behind the former one, put it at the tail
            ins_seq.append(count)
        else:
            res.append(2)
            ins_seq.insert(0, count)
    return res

if __name__ == '__main__':
    pop_seq = [4,1,5,2,3]
    print sim_deque(pop_seq)
