def intervals(nums):
  '''Given a set of ints, breaks into tuples covering all different intervals
     occurring across the nums.'''

  # initialize a list to collect interval tuples
  interval = []

  # sort the given nums in ascending order
  nums.sort()

  # set a start index
  current_index = 0
  interval_start = 0

  # while the index is less than length of nums, zero-indexed
  while current_index < len(nums) - 1:
    # if the distance between the two adjacent numbers is greater than one
    if nums[current_index + 1] - nums[current_index] > 1:
      # create an interval from interval_start to current index (before gap)
      interval.append((nums[interval_start], nums[current_index]))
      # increment the current index and use it to reset the interval start
      current_index += 1
      interval_start = current_index

    else:
      # otherwise, update current index, moving one farther from index start
      current_index += 1
  interval.append((nums[interval_start], nums[current_index]))
  return interval

print(intervals([1,2,3,5,6,7,9,10,11]))
