s = 'boobohrjwnmoboboh'
counter = 0
for i in range(len(s)):
    if s[i] == "b":
        for j in range(i+1, len(s)):
            if s[j] == "o":
                for k in range(i+2, len(s)):
                    if s[k] == "b":
                        counter += 1
                    break
            break
print ("Number of times bob occurs is: {}".format(counter))
