def is_family(data):
  '''Given a list of parent-child element sublists, returns a boolean of whether
  a family tree is correct'''

  # initialize a family tree, where person is key, heirarchy is value
  tree = {}
  par_val = 0
  chil_val = 0

  # for each parent-child sublist
  for par_chil in data:
      # if parent exists in dictionary
      if par_chil[0] in tree:
          # get that parent value and set to par_val
          par_val = tree[par_chil[0]]
      # otherwise
      else:
          # otherwise, insert into dictionary and set parent value to zero
          tree[par_chil[0]] = 0
          par_val = 0
      # if child in dictionary
      if par_chil[1] in tree:
        # get its value and bind to chil_val
        chil_val = tree[par_chil[1]]
      else:
          # update chil_val and increment by (parent + one)
          chil_val = par_val + 1
          tree[par_chil[1]] = chil_val

      # if parent scores >= to child, or Mike not chile to anyone, not Mikes family tree
      if par_val >= chil_val:
          return False
  if tree['Mike'] == 0:
      return False
  return True

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
      ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Logan']
    ]) == False, 'Can you be a father for your father?'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Jack']
    ]) == False, 'Can you be a father for your brather?'
    assert is_family([
      ['Logan', 'William'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    
