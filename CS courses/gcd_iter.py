'''The greatest common divisor of two positive integers is the largest integer
that divides each of them without remainder. Write an iterative function,
gcdIter(a, b), that implements this idea. One easy way to do this is to begin
with a test value equal to the smaller of the two input arguments, and
iteratively reduce this test value by 1 until you either reach a case where the
test divides both a and b without remainder, or you reach 1.'''

def gcdIter(a, b):

    #Find the smaller input arg
    if a < b:
        test = a
    else:
        test = b

    #If test is greater than 1 and divides both evenly, it is the GCD
    while True:
        if (
         test > 1 and
         a % test == 0 and
         b % test == 0
           ):
           return test

        #1 is the GCD
        elif test == 1:
            return 1

        #Test not the GCD, decrement until found
        else:
            test -= 1

x = gcdIter(21,35)
y = gcdIter(21,22)
print ("The GCD of 21 and 35 is {}".format(x))
print ("The GCD of 21 and 22 is {}".format(y))
