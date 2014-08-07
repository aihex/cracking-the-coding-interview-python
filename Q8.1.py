def fib(n):
  nums = [1,1,2]
  if n <= 3:
    return nums[n]
  for i in xrange(3, n):
    nums.append(nums[i-1] + nums[i-2])
  print nums
  return nums[-1]

if __name__ == '__main__':
  print fib(10)
