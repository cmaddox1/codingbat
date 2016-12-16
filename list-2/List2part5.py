def sum67(nums):
  for i in range(0, len(nums)):
    if nums[i] == 6:
      nums[i] = 0
      for a in range(i+1, len(nums)):
        zeroes = nums[a]
        nums[a] = 0
        if zeroes == 7:
          break
  return sum(nums)