from math import sqrt
lst = list()
num = int(raw_input('Enter a number: '))
if num > 1:
    #look to see if number in range between 2 and user input is prime
    for i in xrange(2, int(sqrt(num))):
        #where number divides evenly into user input
        if num % i == 0:
            #print i
            for j in xrange(2,i):
        #         #where another number divides evenly into first number
                 if i % j == 0:
                     print j
                     for k in xrange(2,j):
                         if j % k == 0:
                             print k
                         else:
                             continue
                 else:
                     continue
        #     #break
        # #where number doesn't divide into user input
        else:
            continue
