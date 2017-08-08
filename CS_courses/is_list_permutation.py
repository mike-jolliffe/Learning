def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''

    # check if the lists are permutations, splitting out str from int for sorting
    strings = (sorted([i for i in L1 if type(i)==str]) ==
               sorted([i for i in L2 if type(i)==str]))

    integers = (sorted([i for i in L1 if type(i)==int]) ==
                sorted([i for i in L2 if type(i)==int]))

    #if the strings and integers are both True (same)
    if strings and integers:
        # check for length zero case
        if len(L1) == 0:
            return (None, None, None)
        else:
            # create an empty dict for counting occurrences
            occurrences = {}

            for i in L1:
                # if the element is already a key in occurrences, increment val
                if i in occurrences:
                    occurrences[i] += 1
                # otherwise, set new key-value in dict
                else:
                    occurrences[i] = 1
            # find the key(s) with the highest occurrences (value)
            most = {key:value for (key,value) in occurrences.items() if value == max(occurrences.values())}

            for i in most:
                # return a tuple of the key, number of occurrences, and key type
                return (i, most[i], type(i))
    else:
        return False

L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']
print(is_list_permutation(L1, L2))
