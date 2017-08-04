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
  unconnected = []
  # for each of the desired pixels, grab its connections
  for i in range(len(ones)-1):
      for j in range(i+1, len(ones)):
          if abs(ones[i][0]-ones[j][0]) < 2 and abs(ones[i][1] - ones[j][1]) < 2:
              connections.append((ones[i], ones[j]))
          else:
              unconnected.extend([(ones[i]), (ones[j])])

  # TODO clean up the unconnected so it's only truly unconnected from the pair
  print (connections)
  print (list(set(unconnected)))

  # TODO return unioned sets or stand-alones
  final = []

  def union(A, B):
      return list(set(A) | set(B))

  for i in range(len(connections)):
      for j in range(i+1, len(connections)):
          if connections[j][0] in connections[i] or connections[j][1] in connections[i]:
              final.append(union(connections[j], connections[i]))

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
