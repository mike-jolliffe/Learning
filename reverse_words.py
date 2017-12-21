class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        reversed_word = ""
        word_counter = 0
        for word in s.split():
            word_counter += 1
            reversed_word += word[::-1]
            if not word_counter == len(s.split()):
                reversed_word += " "

        return reversed_word

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseWords("hehe hehe hehe"))
