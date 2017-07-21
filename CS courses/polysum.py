'''
  A regular polygon has n number of sides. Each side has length s.
  The area of a regular polygon is: (0.25*n*s**2)/(tan(pi/n)).
  The perimeter of a polygon is: length of the boundary of the polygon.
  Write a function called polysum that takes 2 arguments, n and s.
  This function should sum the area and square of the perimeter of the regular
  polygon. The function returns the sum, rounded to 4 decimal places.'''

from math import pi, tan

def polysum(n,s):
    #calculate area
    area = (0.25 * n * s ** 2) / (tan(pi/n))

    #calculate square of perimeter
    perimeter = n * s
    perim_sq = perimeter ** 2

    #calculate polysum
    return round(area + perim_sq, 4)

print(polysum(5,6))
