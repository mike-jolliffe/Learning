def key_with_most_vals(aDict):
  '''write a procedure, called biggest, which returns the key corresponding to the
  entry with the largest number of values associated with it. If there is more
  than one such entry, return any one of the matching keys.'''

  new_dict = {}

  #without using k,v and .items()
  for key in aDict:
    counter = 0

    for val in aDict[key]:
      counter += 1
      new_dict[key] = counter

    values = new_dict.values()
    best = max(values)
    keys = []
    for key in new_dict:
      if new_dict[key] == best:
        keys.append(key)

  print (', '.join(keys))

key_with_most_vals({'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'],
                    'd': ['donkey', 'dog', 'dingo']})
