def brackets_checker(string):
  '''Returns a boolean when given an expression as a string. Checks to make sure
  brackets, parentheses, and braces are closed properly'''

  # initialize counters for all types of brackets
  opens = ['[', '{', '(']
  closes = [']', '}', ')']
  brackets = 0

  # if the character is an opener, increment by one, if closer, decrement by one
  for char in string:
      if char in opens:
          brackets += 1
      elif char in closes:
          brackets -= 1

  if brackets == 0:
      return True
  else:
      return False
