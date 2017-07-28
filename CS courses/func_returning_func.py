def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    def poly_part(x):
        """ calculates the polynomial value given coefficient x"""
        # create a sum variable
        total = 0

        # initialize k, which is the total number of elements minus 1 (want to end on zero)
        k = len(L) - 1

        # for every coefficient element, n, in the list
        for n in L:
            # add its value to the total
            total += (n * x ** k)
            k -= 1
        return total

    return poly_part

print(general_poly([1, 2, 3, 4])(10))
