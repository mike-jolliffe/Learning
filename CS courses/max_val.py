def max_val(t):
    """ t, tuple
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    # convert everything to same type, a list
    if type(t) == tuple:
        t = list(t)
    for elmnt in t:
        if type(elmnt) == tuple:
            elmnt = list(elmnt)

    if t == [] or t == ():
        return list(t)

    if type(t[0]) == int:
        return t[:1] + max_val(list(t[1:]))
    return max_val(t[0]) + max_val(list(t[1:]))

print(max_val((1, 2, [5, 6, (1, 2, 9), 7], 2, 3)))
