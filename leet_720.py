class Solution(object):
    def __init__(self):
        self.len_dict = None
        self.words = []

    def longestWord(self, words):
        """Returns longest word that can be built one char at a time from words
        :type words: List[str]
        :rtype: str
        """

        # Create dictionary that stores words by count
        len_dict = {}
        for word in words:
            len_dict.setdefault(len(word), []).append(word) # key might exist already
        self.len_dict = len_dict

        min_val = 'z'
        # For all length one values
        for char in self.len_dict[1]:
            # Look up if longer word can be constructed from them
            val = self.get_longer_word(char)
            # If the return value was not None, and it's smaller than current
            if val and val < min_val:
                # Store it as current min value
                min_val = val
        # For all constructable words
        if self.words:
            # Get the longest one with the lowest lexicographic value
            max_len = max([len(word) for word in self.words])
            return min([word for word in self.words if len(word) == max_len])
        # If no longer word was constructable
        else:
            return min_val

    def get_longer_word(self, shorter_word):
        """Given a shorter word, searches the next longer dictionary key for
        a word that can be constructed from shorter word (e.g., given "app",
        will return "appl")
        :type shorter_word: str
        :rtype: str | None
        """
        found = False
        # If dictionary has longer words
        try:
            # Get list of all words one char longer than input word
            longer_word_list = self.len_dict[len(shorter_word) + 1]
            for word in longer_word_list:
                # If input word is within one of the longer words
                if shorter_word in word and not word in self.words:
                    # Keep it
                    self.words.append(word)
                    # Use it to get an even longer word
                    self.get_longer_word(word)
                    found = True
            # If no word in the longer_word_list contains input word
            if not found:
                # Return the input word
                return shorter_word
        # If no longer words in dictionary
        except KeyError:
            return None


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))  # apple
    sol2 = Solution()
    print(sol2.longestWord(["b","br","bre","brea","break","breakf","breakfa",
    "breakfas","breakfast","l","lu","lun","lunc","lunch","d","di","din","dinn",
    "dinne","dinner"]))  # breakfast
    sol3 = Solution()
    print(sol3.longestWord(["ts","e","x","pbhj","opto","xhigy","erikz","pbh",
    "opt","erikzb","eri","erik","xlye","xhig","optoj","optoje","xly","pb","xhi",
    "x","o"]))  # e
