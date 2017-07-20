lst = list()
num_sum = 0
#Capture all multiples of 3 or 5 below 1000 in a list
for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        lst.append(x)
    else:
        continue
for num in lst:
    num_sum = num_sum + num
print num_sum
