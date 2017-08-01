def genPrimes():
  '''Generator that returns the sequence of prime numbers on successive calls to
  its next() method'''

  # set initial prime value
  p1 = [2]
  next = 2

  while True:

    # set a prime placeholder
    prime = True

    # set the value of next as the last value in the list plus one
    next += 1

    # for each value in the list
    for i in p1:
        # if new number, next, can be divided by it, new number isn't prime
        if next % i == 0:
            prime = False
            break

    if prime == True:
      p1.append(next)
      yield next
