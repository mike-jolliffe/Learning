class Solution:
    def isAnagram(self, s, t):
        """Checks whether t is valid anagram of s
        :type s: str
        :type t: str
        :rtype: bool
        """

        s = list(s)
        t = list(t)
        # For each letter in t
        for char in t:
            # Try removing that letter once from s
            try:
                s.remove(char)
            # Letter is not in s
            except:
                return False
        # If leftover letters in s, return False
        if s:
            return False
        # Valid anagram
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isAnagram("baby", "bab"))  # False
    print(sol.isAnagram("baby", "baby"))  # True
    print(sol.isAnagram("bab", "baby"))  # False
