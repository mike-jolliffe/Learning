def max_val(t):
    """ t, tuple
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """

    if t == [] or t == ():
        return t

    elif type(t) == int:
        return t

    # if this is the final element, return it
    # TODO figure out how to recursively call this
    else:
        m = max_val(t[0])
        return m


print(max_val((1, 2, [5, 6, (1, 2, 9), 7], 2, 3)))
print (max_val((9, [3, 8, 2])))
