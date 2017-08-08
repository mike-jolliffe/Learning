def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """

    # create an empty dictionary
    int_occurs = {}

    # for each element in the list
    for val in L:
        # if it's already a key in the dict, increment the existing value
        if val in int_occurs:
            int_occurs[val] += 1
        # otherwise give it a new key-value
        else:
            int_occurs[val] = 1

    # create list of keys that have odd vals, return max of that list
    key_list = [key for (key, value) in int_occurs.items() if value % 2]
    if len(key_list) == 0:
        return None
    else:
        return max(key_list)


print(largest_odd_times([1,2,3,3,4,4,5,5,5,6,7,8,8,9,9,9,10,11,12]))
