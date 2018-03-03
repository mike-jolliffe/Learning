class Solution:
    def firstUniqChar(self, s):
        """Return index of first char in string occurring only once
        :type s: str
        :rtype: int
        """
        # Remove any duplicates from the string
        uniques = self.del_dupes(s)
        # Handle the empty-string case (all dupes or empty on input)
        if not uniques:
            return -1
        else:
            # Return the first-occurring letter
            for_match = uniques[0]
            # Match that letter to its index
            for char_ix in range(len(s)):
                if s[char_ix] == for_match:
                    return char_ix

    def del_dupes(self, s):
        """Eliminates all duplicate values from string
        :type s: str
        :rtype: str
        """
        # If all chars in s are unique, pass it back
        if str(set(s)) == s:
            return s
        else:
            # Store first char
            try:
                first_char = s[0]
            except IndexError:
                return None

            # For remaining chars after first
            for char in s[1:]:
                # If any are same as first, remove them
                if char == first_char:
                    s = s.replace(first_char, "")
                    return self.del_dupes(s)
            # If first char is unique, pass the string back
            return s


if __name__ == '__main__':
    sol = Solution()
    print(sol.firstUniqChar("loveleetcode"))  # 2
    print(sol.firstUniqChar(""))  # -1
    print(sol.firstUniqChar("aabbcc"))  # -1
