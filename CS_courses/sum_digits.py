def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """

    digits = [int(num) for num in s if num.isnumeric()==True]
    if len(digits) > 0:
        return sum(digits)
    else:
        raise ValueError("ValueError raised")


print(sum_digits("abc34d5"))
print(sum_digits("abcde"))
