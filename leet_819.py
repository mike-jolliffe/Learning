from collections import defaultdict
import string

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """Return most frequently occurring, non-banned word
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # Strip all punctuation
        table = paragraph.maketrans({key: None for key in string.punctuation})
        paragraph = paragraph.translate(table)
        # Make frequency dict for words
        freq_dict = defaultdict(int)
        for word in paragraph.split():
            freq_dict[word.lower()] += 1
        # Sort by frequencies descending
        s = [(k, freq_dict[k]) for k in sorted(freq_dict, key=freq_dict.get, reverse=True)]
        # Return the first (most frequent) non-banned word
        for k, v in s:
            if k not in banned:
                return k


if __name__ == '__main__':
    sol = Solution()
    print(sol.mostCommonWord("Test. test the. punctuation' stripper!?? works, works works", []))  # works
    print(sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))  # ball
