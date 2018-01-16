class Solution:
    def findTheDifference(self, s, t):
        """Returns a string of letters from t not in s
        :type s: str
        :type t: str
        :rtype: str
        """

        for char in s:
            t = t.replace(char, "", 1)
        return t


if __name__ == '__main__':
    sol = Solution()
    print(sol.findTheDifference("abcd", "abcde"))
