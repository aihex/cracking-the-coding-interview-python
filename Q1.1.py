def isunique(s):
  from bitarray import bitarray
  bits = bitarray(256)
  bits.setall(False)
  for i in s:
    idx = ord(i)
    if bits[idx]:
      return False
    bits[idx] = True
  return True




if __name__ == '__main__':
  s = 'abcdefghijklmnopqrstuvwxyzABCD12345678900'
  print isunique(s)
