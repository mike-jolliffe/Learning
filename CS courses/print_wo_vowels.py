def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''

    # create list of vowels, whitespace
    keepers = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

    # create a new, empty string
    new_string = ""

    if len(s) == 0:
        print (new_string)
    else:
        for char in s:
            if char not in keepers:
                new_string += char

        print (new_string)

print_without_vowels("How you doing today!")
