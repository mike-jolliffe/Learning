def brackets_checker(string):
  '''Returns a boolean when given an expression as a string. Checks to make sure
  brackets, parentheses, and braces are closed properly'''

  # create dict of opening and closing bracket types
  brack_types = {'[': ']', '{': '}', '(': ')'}

  # isolate only the bracket types
  all_bracks = [char for char in string if char in brack_types.keys() or char in brack_types.values()]

  # if no brackets, no issues, return True
  if len(all_bracks) == 0:
      return True

  # check if length of all brackets list is even (i.e. number of opens and closes equal)
  if not (len(all_bracks)) % 2 == 0:
    return False

  while True:
      # set a variable to control the outer loop
      is_looping = True

      # for each bracket in the list of brackets
      for i in range(len(all_bracks)):
          # if the starting bracket is an opener
          if all_bracks[i] in brack_types:
              # move through from there to next bracket
              for j in range(i+1, (len(all_bracks))):
                  # if the next bracket is also an opener
                  if all_bracks[j] in brack_types:
                      # break inner loop, move forward in outer loop
                      break
                  # otherwise if it's the correct closer
                  elif brack_types[all_bracks[i]] == all_bracks[j]:
                      # grab the indexes of the bracket pair
                      exclude = [i, j]
                      # create a new list from the old, excluding the pair indexes
                      all_bracks = [all_bracks[c] for c in range(len(all_bracks)) if c not in exclude]
                      # if all brackets successfully paired and removed, return True
                      if len(all_bracks) == 0:
                          return True
                      #in the case of successful pair removal, break both loops, start over
                      is_looping = False
                      break
                  # otherwise, it's the wrong kind of closer
                  else:
                      return False
              # if inner loop broken b/c of pair match, break outer loop too
              if not is_looping:
                  break
          # the starting bracket is a closer
          else:
              return False





print(brackets_checker("{{{[[[[[((((({[{{{{[[[[[[(((((((([[[[[]]]]]))))))))]]]]]]}}}}]})))))]]]]]}}}")) # even, should return True
#print(brackets_checker("Hello {( world }[")) # even, should return False
#print(brackets_checker("Hello {( world }")) # odd, should return False
#print(brackets_checker("Hello ] (world )")) # even, triggers False in Except
#assert brackets_checker("((5+3)*2+1)") == True, "Simple"
#assert brackets_checker("{[(3+1)+2]+}") == True, "Different types"
#assert brackets_checker("(3+{1-1)}") == False, ") is alone inside {}"
#assert brackets_checker("[1+1]+(2*2)-{3/3}") == True, "Different operators"
#assert brackets_checker("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
#assert brackets_checker("2+3") == True, "No brackets, no problem"
