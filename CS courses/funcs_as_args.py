def f(i):
    return i + 2

def g(i):
    return i > 5

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer
    g takes in an integer, applies a Boolean function,
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """

    # make sure L is a list
    assert type(L) == list and len(L) > 0, "Improper input of L."
    # create a copy for iterating, so removal doesn't mess up index
    iterable = L.copy()
    # for each element in L
    for i in iterable:
        #check return types on f() and g()
        assert type(i) == int, "L is not a list of integers"
        assert type(f(i)) == int, "Return type for f() not an int"
        assert type(g(i)) == bool, "Return type for g() not a bool"
        # if g(f(element)) returns False:
        if g(f(i)) == False:
            # remove i
            L.remove(i)

    # if L is empty:
    if L == []:
        # return -1
        return -1
    # otherwise return the max value within L
    else:
        return max(L)

L = [1,2,3,4,5]
print(applyF_filterG(L, f, g))
print(L)
