def connected_pixels(list_of_ij):
  '''Input: list of lists with elements 0 or 1.
  Returns a list of counts representing sizes of pixel clusters with desired attribute'''


  # get the i,j index of all pixels with desired attribute, 1
  ones = []
  for i in range(len(list_of_ij)):
      for j in range(len(list_of_ij[i])):
          if list_of_ij[i][j] == 1:
              ones.append((i,j))

  # for each of the desired pixels, grab its connections
  connections = []
  unconnected = []
  for i in range(len(ones)-1):
      for j in range(i+1, len(ones)):
          if abs(ones[i][0]-ones[j][0]) < 2 and abs(ones[i][1] - ones[j][1]) < 2:
              connections.append((ones[i], ones[j]))
          else:
              unconnected.extend([(ones[i]), (ones[j])])
  #print (connections)


  # return unioned sets of connected pixels
  # TODO figure out how to reduce final to single occurrences of values
  unions = []

  def union(A, B):
      if any(i in B for i in A):
          return list(set(A) | set(B))


  for i in range(len(connections)):
      for j in range(i+1, len(connections)):
          unions.append(union(connections[j], connections[i]))

  final = []
  for elmnt in unions:
      if not elmnt in final and elmnt != None:
          final.append(elmnt)
  #print (final)

  # clean up unconnected 
  # TODO clean up the unconnected so it's only truly unconnected from the pair
  final_unconnected = []
  for u in unconnected:
      for c in final:
          if u not in c and u not in final_unconnected:
              print (u,c)
              final_unconnected.append(u)
              break
  #print (final_unconnected)
  # for each element in the list, get its length and append it to a counts list

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
