def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    # Firest, reverse the main list in-place
    L.reverse()

    # Then for each sublist
    for lst in L:
        #reverse it
        lst.reverse()

    print (L)

deep_reverse([[1,2,3],[4,5,6],[7,8,9]])
