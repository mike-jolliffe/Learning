'''We can use the idea of bisection search to determine if a character is in a
   string, so long as the string is sorted in alphabetical order. First, test
   the middle character of a string against the character you're looking for
   (the "test character"). If they are the same, we are done - we've found the
   character we're looking for! If they're not the same, check if the test
   character is "smaller" than the middle character. If so, we need only
   consider the lower half of the string; otherwise, we only consider the upper
   half of the string. (Note that you can compare characters using
   Python's < function.)'''

def isIn(char, aStr):

    #check for empty string case
    if len(aStr) == 0:
        return False

    else:
        #grab middle char from aStr
        half_index = len(aStr)//2
        print ('string is now {} num long'.format(half_index*2))
        mid = aStr[half_index]
        print ('midpoint is letter {}'.format(mid))

        #check for True
        if char == mid:
            return True

        #check for False
        elif half_index == 0:
            return False

        #Otherwise, choose which half to keep, and call isIn on it
        elif char < mid:
            return isIn(char, aStr[:half_index])
        elif char > mid:
            return isIn(char, aStr[half_index:])

print(isIn('e', 'abcdefghijklmnopqrs'))
print(isIn('x', 'abcdefghijklmnop'))
print(isIn('a', 'abcdef'))
print(isIn('p', 'abcdefghijklmnop'))
print(isIn('a', ''))
