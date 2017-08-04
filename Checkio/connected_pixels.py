def connected_pixels(list_of_ij):
  '''Input: list of lists with elements 0 or 1.
  Returns a list of counts representing sizes of pixel clusters with desired attribute'''

  # initialize holder for pixel values of 1
  ones = []
  # get the i,j index of all pixels with desired attribute, 1
  for i in range(len(list_of_ij)):
      for j in range(len(list_of_ij[i])):
          if list_of_ij[i][j] == 1:
              ones.append((i,j))

  # create a holder for storing connected desireds
  connections = []
  # for each of the desired pixels, grab its connections
  for i in range(len(ones)-1):
      for j in range(i+1, len(ones)):
          if abs(ones[i][0]-ones[j][0]) < 2 and abs(ones[i][1] - ones[j][1]) < 2:
              connections.append((ones[i], ones[j]))
          else:
              connections.extend([(ones[i]), (ones[j])])
  print (connections)

  # TODO fix the following code so it returns unioned sets or stand-alones
  final = []
  # create unions from the individual connections so not double counting
  for i in range(len(connections)):
      for j in range(i+1, len(connections)):
          if connections[j][0] in connections[i] or connections[j][1] in connections[i]:
              final.append(list(set(connections[j]) | set(connections[i])))

  print (final)

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
