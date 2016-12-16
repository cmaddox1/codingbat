def centered_average(nums):
  a=sum(nums)-min(nums)-max(nums)
  b=len(nums)-2
  c=a/b
  return c