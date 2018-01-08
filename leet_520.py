class Solution:
    def detectCapitalUse(self, word):
        """Checks if capitalization is proper (all caps, first letter, or none)
        :type word: str
        :rtype: bool
        """

        # Check for no upper or all upper
        if all(l.isupper() for l in word) or all(l.islower() for l in word):
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.detectCapitalUse('flAg'))  # False
    print(sol.detectCapitalUse('Flag'))  # True
    print(sol.detectCapitalUse('flag'))  # True
    print(sol.detectCapitalUse('FLAG'))  # True
