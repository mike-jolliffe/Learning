class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """Returns next greatest letter from target in sorted list. Wraps around.
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # Iterate through list until first larger char or end
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreatestLetter(['c','f','j'], 'd'))  # f
    print(sol.nextGreatestLetter(['c','f','j'], 'f'))  # j
    print(sol.nextGreatestLetter(['c','f','j'], 'j'))  # c
