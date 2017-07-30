def intervals(nums):
  '''Given a set of ints, breaks into tuples covering all different intervals
     occurring across the nums.'''

  # initialize a list to collect interval tuples
  interval = []
  nums.sort()
  interval_start = 0

  # for a given pair in nums, if interval between them > 1
  for i in range(len(nums)-1):
    interval_start = nums[i]
    for j in range(i:len(nums)):
      # set an intermediate place-holder
      interval_continue = interval_start
      # if distance between adjacent nums > 1
      if nums[j] - nums[i] > 1:
        # capture the interval
        interval.append((interval_start, nums[j]))
      else:

      # break the loop
      break

  # otherwise, append that item into an interval

  # for the interval, sort ascending and convert to a tuple of max, min
