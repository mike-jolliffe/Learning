def connected_pixels(list_of_ij):
  '''Input: list of lists with elements 0 or 1.
  Returns a list of counts representing sizes of pixel clusters with desired attribute'''

  # initialize holder for pixel values of 1
  ones = []
  # get the i,j index of all pixels with desired attribute, 1
  for i in range(len(list_of_ij)):
      for j in range(len(list_of_ij[i])):
          if list_of_ij[i][j] == 1:
              ones.append([i,j])
  print(ones)
  # create a holder for storing connected desireds
  connections = []
  # for each of the desired pixels, compare others to it to see if connected

  # store the connected

connected_pixels([
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0],  # should be [[1,2],[1,3],[2,3],[3,1]]
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]])
connected_pixels([
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],  # should be [[1,2],[1,3],[2,3][3,1],[3,2]]
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0]])
