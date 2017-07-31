def is_family(data):
  '''Given a list of parent-child element sublists, returns a boolean of whether
  a family tree is correct'''

  # initialize a family tree, where person is key, heirarchy is value
  tree = {}


  # for each parent-child sublist
  for par_chil in data:
      # if parent in dictionary
      if not par_chil[0] in tree:
          # increment by one
          tree[par_chil[0]] = 0

      # if child in dictionary
      if par_chil[1] in tree:
          # add its parent score, and increment by one
          tree[par_chil[1]] += (tree[par_chil[0]]+1)
      else:
          tree[par_chil[1]] = (tree[par_chil[0]]+1)

  for par_chil in data:
      if tree[par_chil[0]] > tree[par_chil[1]]:
          return False
  return True

print(is_family([["Logan","Mike"],["Logan","Jack"]]))
