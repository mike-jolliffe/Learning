class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        kbRow_dict = {1: "qwertyuiop",
                      2: "asdfghjkl",
                      3: "zxcvbnm"}

        one_row_words = []
        for word in words:
            row = []
            for letter in word.lower():
                val = [key for key, value in kbRow_dict.items() if letter in value][0]
                row.append(val)
            if all(sub_row == 1 for sub_row in row) or \
               all(sub_row == 2 for sub_row in row) or \
               all(sub_row == 3 for sub_row in row):
               one_row_words.append(word)

        return one_row_words

if __name__ == '__main__':
    sol = Solution()
    print(sol.findWords(["Hello", "Alaska", "Dad", "Peace"]))
