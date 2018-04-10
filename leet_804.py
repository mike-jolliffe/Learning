class Solution(object):
    def __init__(self):
        self.morse_dict = {"a":".-","b":"-...","c":"-.-.","d":"-..",
                           "e":".","f":"..-.","g":"--.","h":"....",
                           "i":"..","j":".---","k":"-.-","l":".-..",
                           "m":"--","n":"-.","o":"---","p":".--.",
                           "q":"--.-","r":".-.","s":"...","t":"-",
                           "u":"..-","v":"...-","w":".--","x":"-..-",
                           "y":"-.--","z":"--.."}
        self.morse_words = []

    def uniqueMorseRepresentations(self, words):
        """Return the number of unique Morse code patterns from a list of words
        :type words: List[str]
        :rtype: int
        """
        # Create a morse word by concatenating letters
        morse_word = ""
        for word in words:
            for char in word:
                morse_word = morse_word + self.morse_dict[char]
            # Append morse word to list of morse words
            self.morse_words.append(morse_word)
            morse_word = ""
        # Get the number of unique morse words
        return len(set(self.morse_words))


if __name__ == '__main__':
    sol = Solution()
    print(sol.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))  # 2
