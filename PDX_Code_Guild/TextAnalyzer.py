import string
import sys

class TextAnalyzer():
    '''

    Allow the user to enter a word and get the most likely words to follow the given word. Store the pair counts as a dict
    of dicts, where the first key is the first word in the pair and the second key is the second word.

    EX: Enter Query Word > Mr.
        The most likely bi - gram pair starting
        with "Mr." is "Mr. Darcy".


    Redo the pair counts: normalize the probabilities in the inner dict by the count of pairs that start with the first word.

    Chain together that ability to generate random sentences, one word at a time, from a given starting word.'''

    def __init__(self, input_file):
        self.input_file = (open(input_file)).read()

        # for getting all individual words and storing their occurrence frequency
        self.words_array = []
        self.count = {}

        # for getting all word pairs and storing their occurrence frequency
        self.pairs_array = []
        self.pairs_count = {}

    def loadWords(self):
        '''returns an array of words with capitalization, punctuation, and non-printables removed'''

        # get rid of non-printable chars like non-ASCII smartquotes, newlines, etc.
        clean_words = ''.join(list(filter(lambda x: x in string.printable, self.input_file)))

        # get rid of punctuation
        translator = str.maketrans('', '', string.punctuation)
        clean_words = clean_words.translate(translator)

        # lowercase and split string. Put all the words into an array
        self.words_array.extend((clean_words.lower()).split())

    def word_count(self):
        '''counts the occurrence of each word in the document'''
        for word in self.words_array:
            if not word in self.count:
                self.count[word] = 1
            else:
                self.count[word] += 1
        return self.count

    def most_common(self):
        '''returns the top ten single word-occurrence tuples'''
        most_freq = [(k, self.count[k]) for k in sorted(self.count, key=self.count.get, reverse=True)]
        return most_freq[:11]

    def get_pairs(self):
        '''returns all adjacent word pairs in the document'''
        for i in range(len(self.words_array)-1):
            for j in range(i+1, i+2):
                self.pairs_array.append((self.words_array[i],self.words_array[j]))
        return self.pairs_array

    def pairs_frequency(self):
        '''builds a frequency dictionary for word pairs'''
        for pair in self.pairs_array:
            if not pair in self.pairs_count:
                self.pairs_count[pair] = 1
            else:
                self.pairs_count[pair] += 1
        return self.pairs_count

    def pairs_most_common(self):
        '''returns the top ten word-pair occurrence tuples'''
        most_freq = [(k, self.pairs_count[k]) for k in sorted(self.pairs_count, key=self.pairs_count.get, reverse=True)]
        return most_freq[:11]

if __name__ == '__main__':
    translator = TextAnalyzer(sys.argv[1])
    translator.loadWords()
    translator.word_count()
    #print(translator.most_common())
    translator.get_pairs()
    translator.pairs_frequency()
    print(translator.pairs_most_common())
