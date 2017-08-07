def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain
                          N unique lowercase letters.
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where
        each key is a letter in map_from at index i and the corresponding
        value is the letter in map_to at index i.
        decoded is a string that contains the decoded version
        of code using the key_code mapping. """

    # Build a dictionary called key_code that captures mapping of map_from:map_to
    key_code = {}
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]

    return key_code
    # Create variable, decoded, to which cipher dict is applied

    # Return key_code and decoded string

print(cipher("abcd", "dcba", "dab")) 
