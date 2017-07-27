def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    if aList == []:
        return aList

    if isinstance(aList[0], list):
        return flatten(aList[0]) + flatten(aList[1:])

    return aList[:1] + flatten(aList[1:])


def printer(lst):
    '''takes result of flatten() and prints it'''
    print(lst)


printer(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))
