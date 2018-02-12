class Solution:
    def canConstruct(self, ransomNote, magazine):
        """Check whether ransomNote can be constructed from magazine letters
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # For each letter in ransom note remove that letter from magazine
        for letter in ransomNote:
            if letter in magazine:
                magazine = magazine.replace(letter, '', 1)
            # Letter isn't in magazine or has already been used
            else:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.canConstruct("aa", "aab"))  # True
    print(sol.canConstruct("aa", "ab"))  # False
