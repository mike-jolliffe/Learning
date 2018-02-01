class Solution:
    def countSubstrings(self, s):
        """Return number of palindromic substrings occurring in given string
        :type s: str
        :rtype: int
        """

        # Generate list of all substrings forward
        forward_subs = self.makeSubstrings(s)

        # Find the intersection of the two lists (forward same as backward)
        palindrome = []
        for sub in forward_subs:
            if sub == sub[::-1]:
                palindrome.append(sub)
        print(palindrome)
        return len(palindrome)

    def makeSubstrings(self, s):
        """Generate all possible substrings from s
        :type s: string
        :rtype: List[string]
        """

        subs_list = []
        for start in range(len(s)):
            for stop in range(start, len(s)):
                subs_list.append(s[start:stop + 1])
        return subs_list


if __name__ == '__main__':
    sol = Solution()
    # print(sol.makeSubstrings("abc"))  # [a,b,c,ab,bc,abc]
    print(sol.countSubstrings("abc"))  # 3
    print(sol.countSubstrings("aaa"))  # 6
    print(sol.countSubstrings("aba"))  # 4
