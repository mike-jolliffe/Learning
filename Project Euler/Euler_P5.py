i = 200000000
divisor = False
while i < 250000000:
    for j in range(2, 20):
        if i % j > 0:
            divisor = False
            break
        else:
            divisor = True
    if divisor == True:
        print i
    i += 2
print "hit 250000000"
