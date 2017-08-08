def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary, d2, whose keys are the unique values from d,
    and whose values are a sorted (ascending) list of d's keys
    '''

    # create an empty dict
    new_dict = {}
    # for each old_key in the original dictionary
    for old_key in d:
        # if its old_value is a key in new dict
        if d[old_key] in new_dict:
            # add the old_key as a new_value in new dict
            new_dict[d[old_key]].append(old_key)
        # otherwise add the old_value and old_key as k, v pair
        else:
            new_dict[d[old_key]] = [old_key]

    #sort the vals list for each key
    new_dict = {key: sorted(value) for (key, value) in new_dict.items()}

    # return the result
    return new_dict

print(dict_invert({3: True, 4: True, 5: False, 1: True, 9: False}))
