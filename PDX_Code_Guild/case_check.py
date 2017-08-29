def case_check(word):
    '''returns a CamelCase/Snake_case check'''
    index_list = []
    for char in word:
        if char.isupper():
            index_list.append(word.index(char))
    if len(index_list) > 1:
        return f"CamelCase"
    if "_" in word:
        return f"Snake_case"

print(case_check("CamelCase"))
print(case_check("snake_case"))
