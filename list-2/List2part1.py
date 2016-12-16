def count_evens(nums):
  a=[]
  for i in nums:
    if i % 2 == 0:
      a.append(i)
  return len(a)