s = 'azcbobobegghakl'
new_str = ''
longest_str = ''
for char in s:
    if (new_str == '' or char >= new_str[-1]):
        new_str = new_str + char
        if len(new_str) > len(longest_str):
            longest_str = new_str
    else:
        new_str = char

print ("Longest substring in alphabetical order is: {}".format(longest_str))
