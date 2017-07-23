'''Write a procedure called oddTuples, which takes a tuple as input, and returns
   a new tuple as output, where every other element of the input tuple is copied,
   starting with the first one.'''

def odd_tups(aTup):
    #create new tuple to receive every other element from input
    new_tup = ()

    for i in range(len(aTup)):
        #check if index is even (first element is odd, despite evenly indexed)
        if i % 2 == 0:
            #can only concatenate tuple to tuple, so include comma
            new_tup += (aTup[i],)
    print (new_tup)

odd_tups((1,2,3,4,5,6,7))
