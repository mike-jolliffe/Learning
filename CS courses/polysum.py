from math import pi, tan

def polysum(n,s):
    '''Inputs:
         n, an integer representing the number of sides a polygon has
         s, and integer or float representing the length of each side
       Output:
         The polygon's area plus the square of its perimeter, rounded to
         four digits'''

    #calculate area
    area = (0.25 * n * s ** 2) / (tan(pi/n))

    #calculate square of perimeter
    perimeter = n * s
    perim_sq = perimeter ** 2

    #calculate polysum, rounded to four digits
    return round(area + perim_sq, 4)
