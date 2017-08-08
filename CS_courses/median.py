def median(num_list):
  '''this function takes a list of natural numbers and calculates the median'''

  midpoint = len(num_list) // 2
  num_list.sort()
  print(num_list)

  if len(num_list) % 2 == 0:
      print ("even")
      print (num_list[midpoint - 1] + num_list[midpoint]) / 2.0
  else:
      print ("odd")
      print (num_list[midpoint])

median([1,2,3,4,5])

median([1,2,3,4,5,6])
