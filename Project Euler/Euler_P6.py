#Sum of the squares (A)
x = 0
for i in range(1,101):
    x = x + i**2
A = x
#Square of the Sum (B)
y = 0
for i in range(1,101):
    y+=i
B = y**2
#Difference (B - A)
Diff = B - A
print Diff
