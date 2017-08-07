def max_val(t):
    """ t, tuple
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """

    # if this is the final element, return it
    if len(t) == 1:
        return t[0]

    # otherwise, call max_val on it, returning the greater value
    else:
        m = max_val(t[1:])
        if type(t[0]) == int:
            return m if m > t[0] else t[0]
        else:
            return max_val(t[0])

print(max_val((1, 2, [5, 6, (1, 2, 9), 7], 2, 3)))
print (max_val((9, [3, 8, 2])))
