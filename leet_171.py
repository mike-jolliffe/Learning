class Solution:
    def titleToNumber(self, s):
        """Return column number in Excel sheet when given string of alphabetic characters
        :type s: str
        :rtype: int
        """

        # Split and reverse string so 0s place is farthest left
        s = list(s)
        s.reverse()
        # Mod everything by 64 so A is 1 
        base_26_digits = list(map(lambda x: ord(x) % 64, s))
        return sum([base_26_digits[i] * 26 ** i for i in range(len(base_26_digits))])

if __name__ == '__main__':
    sol = Solution()
    print(sol.titleToNumber("A"))  # 1
    print(sol.titleToNumber("Z"))  # 26
    print(sol.titleToNumber("AA"))  # 27
    print(sol.titleToNumber("BA"))  # 53
