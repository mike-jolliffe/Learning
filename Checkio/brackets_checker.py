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

  # set a value for starting bracket
  starting_bracket = ""

  while True:
      print(len(all_bracks))
      # for each bracket in the list of brackets
      for i in range(len(all_bracks)):
          # if the starting bracket is in the dictionary keys
          if starting_bracket in brack_types:
              # if the all_bracks bracket is a closer that complements the starting bracket
              if brack_types[starting_bracket] == all_bracks[i]:
                  # remove the pair of brackets from the list and start over
                  all_bracks.remove(all_bracks[i])
                  all_bracks.remove(starting_bracket)
                  if len(all_bracks) == 0:
                      return True
                  break
              # if the bracket is an opener, set it as the new starting bracket
              elif all_bracks[i] in brack_types.keys():
                  starting_bracket = all_bracks[i]
              else:
                  print ("False 1")
                  return False
          # if the starting_bracket isn't in the dictionary keys but is empty
          elif starting_bracket == "":
              # assign its first value
              starting_bracket = all_bracks[i]
          # the starting bracket is a closer
          else:
              print("False 2")
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
