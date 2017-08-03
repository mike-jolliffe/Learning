def brackets_checker(string):
  '''Returns a boolean when given an expression as a string. Checks to make sure
  brackets, parentheses, and braces are closed properly'''

  # create dict of opening and closing bracket types
  brack_types = {'[': ']', '{': '}', '(': ')'}

  # isolate only the bracket types
  all_bracks = [char for char in string if char in brack_types.keys() or char in brack_types.values()]
  print(all_bracks)
  # check if length of all brackets list is even (i.e. number of opens and closes equal)
  if len(all_bracks) % 2 == 0:
    # if it is, divide list in half, flip left half so can start from inside out
    left_half = all_bracks[:int(len(all_bracks) / 2)]
    left_half = left_half[::-1]
    right_half = all_bracks[int(len(all_bracks) / 2):]
    print (left_half)
    print (right_half)
    exit()
  else:
    return False
  # compare elements pair-wise
  for i in range(len(right_half)):
      # if the left_half element is a key in the dictionary
      if left_half[i] in brack_types.keys():
          # compare the associated dictionary value at that key to the right hand element
          if not brack_types[left_half[i]] == right_half[i]:
              return False
      # if the left_half element is a value in the dictionary
      elif left_half[i] in brack_types.values():
          # compare the associated dictionary key at that value to the right hand element
          if not brack_types[right_half[i]] == left_half[i]:
              return False
  return True

print(brackets_checker("Hello {( world )}[]")) # even, should return True
print(brackets_checker("Hello {( world }[")) # even, should return False
print(brackets_checker("Hello {( world }")) # odd, should return False
