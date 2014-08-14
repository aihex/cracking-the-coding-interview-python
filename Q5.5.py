def req_one(a, b):
    c = a ^ b
    count = 0
    while c:
        if c & 1:
            count += 1
        c >>= 1
    return count

if __name__ == '__main__':
    print req_one(7, 0xfffff)
