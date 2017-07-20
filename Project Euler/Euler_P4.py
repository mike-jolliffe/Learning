#find all products of 3-digit nums
biggest_pal = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        num = str(i*j)
        if num[0]+num[1]+num[2] == num[-1]+num[-2]+num[-3]:
            print num
            if int(num) > biggest_pal:
                biggest_pal = int(num)
                pal1 = i
                pal2 = j
print biggest_pal
print pal1
print pal2
