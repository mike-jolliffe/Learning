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

  # find the first closing bracket
  for brack in all_bracks:
    if brack in brack_types.keys():
      # try stepping back one element
      try:

      except:
        # if you can't, return False
        return False
        
    # if the element is an opening type
        # it must be the same type as the close, or return False
    # if the element is another closing type
        # repeat the above by stepping back an element and checking against new closing type
    # find the next closing bracket in the sequence


print(brackets_checker("Hello {( world )}[]")) # even, should return True
print(brackets_checker("Hello {( world }[")) # even, should return False
print(brackets_checker("Hello {( world }")) # odd, should return False
