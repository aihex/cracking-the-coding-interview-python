def update_bit(m, n, i, j):
  a = (1 << i) - 1
  a &= n
  return (n >> (j+1) << (j+1)) | m << i | a

if __name__ == '__main__':
  n = 1 << 10
  m = 21
  print update_bit(m, n, 0, 0)
