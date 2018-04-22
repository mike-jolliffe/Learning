from collections import deque


class Solution(object):
    def reverseVowels(self, s):
        """Return string with vowel order reversed
        :type s: str
        :rtype: str
        """
        vowels_forward = [char for char in s if char.lower() in 'aeiou']
        # Map vowels to reversed vowels into deque structure
        vowels_mapper = deque([(forward, backward) for forward, backward
                        in zip(vowels_forward, reversed(vowels_forward))])
        for i in range(len(s)):
            # If the char is a vowel
            if s[i] in vowels_forward:
                # Grab first element from deque object (stack and queue generalized)
                new_vowel = vowels_mapper.popleft()[1]
                # Break string apart, swap vowel, put together
                s = s[:i] + new_vowel + s[i+1:]

        return s

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseVowels('leetcode'))
    print(sol.reverseVowels('hello'))
