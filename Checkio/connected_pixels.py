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
  print ("CONNECTED: {}".format(connections))

  # return unioned sets of connected pixels
  def union(A, B):
      print ("A: {}, B: {}".format(A,B))
      if any(i in B for i in A):
          combo = list(set(A) | set(B))
          print ("UNION? {}".format(combo))
          return combo
      else:
          return -1

  # TODO resolve dupes issue
  unions = []
  for i in range(len(connections)):
      full_set = connections[i]
      for j in range(len(connections)):
          new_set = union(connections[j], full_set)
          if new_set != -1:
              full_set = new_set
      if not full_set in unions:
          unions.append(full_set)
  print("FULL SET: {}".format(unions))

  # clean up unconnected
  #TODO figure out why this code doesn't exclude stuff that's in Full set
  final_unconnected = []
  for u in unconnected:
      if not u in full_set and not u in final_unconnected:
          final_unconnected.append(u)
  print ("final_unconnected: {}".format(final_unconnected))

  # merge unioned and unconnected into a final list
  final_set = []
  final_set.append(full_set)
  final_set.append(final_unconnected)
  print ("FINAL SET: {}".format(final_set))

  # for each element in the list, get its length and append it to a counts list
  count = []
  for sub_list in final_set:
      if len(sub_list) > 0:
          count.append(len(sub_list))
  print (sorted(count))


# connected_pixels([
#     [0, 0, 0, 0, 0],
#     [0, 0, 1, 1, 0],
#     [0, 0, 0, 1, 0],  # should be [[1,2],[1,3],[2,3],[3,1]]
#     [0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0]])
# connected_pixels([
#     [0, 0, 0, 0, 0],
#     [0, 0, 1, 1, 0],  # should be [[1,2],[1,3],[2,3][3,1],[3,2]]
#     [0, 0, 0, 1, 0],
#     [0, 1, 1, 0, 0]])
connected_pixels([
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0]])
