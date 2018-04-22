class Solution(object):
    def reverseVowels(self, s):
        """Return string with vowel order reversed
        :type s: str
        :rtype: str
        """
        vowels_forward = [char for char in s.lower() if char in 'aeiou']
        # Map vowels to reversed vowels
        vowels_mapper = {forward: backward for forward, backward
                        in zip(vowels_forward, reversed(vowels_forward))}
        for i in range(len(s)):
            # If the char is a vowel
            if s[i] in vowels_forward:
                # Break string apart, swap vowel, put together
                s = s[:i] + vowels_mapper[s[i]] + s[i+1:]
        return s

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseVowels(''))
