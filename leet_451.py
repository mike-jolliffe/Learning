from collections import Counter

class Solution:
    def frequencySort(self, s):
        """Return s rearranged so letters in descending order of frequency
        :type s: str
        :rtype: str
        """

        # Create unique (char, frequency) tuples and add to list
        letter_freq = []
        for char in s:
            count = s.count(char)
            if not (char, count) in letter_freq:
                letter_freq.append((char, count))

        sorted_s = ""
        # Remove most-frequent chars from list, concat to string, until list empty
        while letter_freq:
            curr_max = max([freq for letter, freq in letter_freq])
            char = [letter for letter, freq in letter_freq if freq == curr_max][0]
            sorted_s += char * curr_max
            letter_freq.remove((char, curr_max))
        return sorted_s


if __name__ == '__main__':
    sol = Solution()
    print(sol.frequencySort("aabbbccDDDDd"))  # DDDDbbbccaad
