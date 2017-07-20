#Find all Fibonacci numbers less than 4 million
lst = [1,2]
num_sum = 0
for i in range(3,4000000):
    if i == lst[-1]+lst[-2]:
        lst.append(i)
for num in lst:
    if num % 2 == 0:
        num_sum = num_sum + num
print num_sum
#sum the even-valued terms
