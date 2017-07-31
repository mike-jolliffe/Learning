def is_family(data):
  '''Given a list of parent-child element sublists, returns a boolean of whether
  a family tree is correct'''

  # initialize a dictionary, where parent is key, child is value
  tree = {}

  # for each parent-child sublist
    # if parent is a key already, add child as value to that key
    # or if parent is a value, replace that value with a key-value sub-dictionary
    # or if child is a key, create new dict key above everything for parent
