def vals_count(dictionary):
  '''Given a dictionary input, outputs total count of values appearing
     across all keys in dictionary, unpacking lists/tuples and grabbing
     individual values.'''

  counter = 0

  for val in dictionary.values():
    if type(val) == str:
      counter += 1
    else:
      for elmt in val:
          counter += 1
  print (counter)

vals_count({'a':'aardvark', 'b':('baboon','beluga'), 'c':['chameleon','cat']})
