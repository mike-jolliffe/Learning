class Solution:
    def replaceWords(self, dictionary, sentence):
        """Given dictionary of word roots, replace words in sentence with roots
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """

        # Split the sentence
        split_sentence = sentence.split()
        # For each word in the sentence
        for i in range(len(split_sentence)):
            # If a root is part of that word
            for root in dictionary:
                if split_sentence[i].startswith(root):
                    # Replace that word
                    split_sentence[i] = root
        return ' '.join(split_sentence)


if __name__ == '__main__':
    sol = Solution()
    print(sol.replaceWords(["cat", "rat", "bat"], "the cattle was rattled by the battery"))
