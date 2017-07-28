def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """

    # A number is triangular if and only if n(n+1)/2 can equal k for some int, n
    n = 0
    max_n = k+1


    while True:
        guess = n * (n+1) / 2
        if guess == k:
            return True
        elif n == max_n:
            return False
        else:
            n += 1

print(is_triangular(10))

print(is_triangular(14))
