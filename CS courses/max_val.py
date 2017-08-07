def max_val(t):
    """ t, tuple
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """

    def flatten(t):
        '''Helper function that takes t and flattens it into a list of ints'''
        if t == [] or t == () or type(t) == int:
            return [t]

        elif len(t) == 1 and type(t[0]) == int:
            return t[:1]

        elif len(t) == 1 and (type(t[0]) == list or type(t[0]) == tuple):
            return flatten(t[0])

        # if this is the final element, return it
        # TODO figure out how to recursively call this
        else:
            return flatten(t[0]) + flatten(list(t[1:]))

    lst = flatten(t)
    return max(lst)

print(max_val((1, 2, [5, 6, (1, 2, 9), 7], 2, 3)))
print (max_val((9, [3, 8, 2])))
