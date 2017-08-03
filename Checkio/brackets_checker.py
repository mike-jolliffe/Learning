def brackets_checker(string):
  '''Returns a boolean when given an expression as a string. Checks to make sure
  brackets, parentheses, and braces are closed properly'''

  # create dict of opening and closing bracket types
  brack_types = {'[': ']', '{': '}', '(': ')'}

  # isolate only the bracket types
  all_bracks = [char for char in string if char in brack_types.keys() or char in brack_types.values()]
  print(all_bracks)

  # check if length of all brackets list is even (i.e. number of opens and closes equal)
  if not len(all_bracks) % 2 == 0:
    return False

  # set a value for stepping back
  steps_back = 1

  # find the first closing bracket
  for i in range(len(all_bracks)):
    # can't have the first bracket be a closing type
    if all_bracks[i] in brack_types.values() and i == 0:
        return False
    # if the first found closing bracket is after index zero
    elif all_bracks[i] in brack_types.values():
      if i - steps_back < 0:
          
      #step back one element and check if element is opening type
      elif all_bracks[i-steps_back] in brack_types.keys():
        # it must be the same type as the close, or return False
        if not brack_types[all_bracks[i-steps_back]] == all_bracks[i]:
          return False
      # if the element is another closing type
      else:
        # repeat the above by stepping back an element and checking against new closing type
        steps_back += 1
  return True




print(brackets_checker("Hello {( world )}[]")) # even, should return True
print(brackets_checker("Hello {( world }[")) # even, should return False
print(brackets_checker("Hello {( world }")) # odd, should return False
print(brackets_checker("Hello ] (world )")) # even, triggers False in Except
