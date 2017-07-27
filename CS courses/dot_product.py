def dotproduct(listA, listB):
  '''
  returns the sum of the pairwise products of listA and listB. Assumes both
  lists are of equal length.
  '''

  #initialize a variable to keep track of the sum
  total = 0

  for i in range(len(listA)):
      total += (listA[i] * listB[i])

  print (total)

dotproduct([1,2,3,4], [5,6,7,8])
