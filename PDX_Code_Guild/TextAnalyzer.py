import string
import sys

class TextAnalyzer():
    '''

    Chain together that ability to generate random sentences, one word at a time, from a given starting word.'''

    def __init__(self, input_file):
        self.input_file = (open(input_file)).read()

        # for getting all individual words and storing their occurrence frequency
        self.words_array = []
        self.count = {}

        # for getting all word pairs and storing their occurrences
        self.pairs_array = []
        self.pairs_count = {}
        self.pre_dict = {}

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

    def prediction_dict(self):
        '''returns a dictionary to be used for predicting next word given a first word'''
        # build occurrence dictionary
        for wordpair, value in self.pairs_count.items():
            if not wordpair[0] in self.pre_dict:
                self.pre_dict[wordpair[0]] = {wordpair[1]:value}
            else:
                self.pre_dict[wordpair[0]].update({wordpair[1]:value})

        # overwrite occurrences with probabilities of second word based on total of all second words
        for word_one in self.pre_dict:
            total_count = sum(self.pre_dict[word_one].values())
            for word_two in self.pre_dict[word_one]:
                self.pre_dict[word_one][word_two] = self.pre_dict[word_one][word_two] / total_count
        return self.pre_dict

    def predict_word(self, word):
        '''returns prediction based on most frequent occurrences following a given word'''

        # build an array next word guesses, with most frequent first
        best_guess = [k for k in sorted(self.pre_dict[word], key=self.pre_dict[word].get, reverse=True)]
        return best_guess

    def make_sentence(self, word, length):
        '''This returns a generated sentence of given length by using a given word as the first word and picking most
        likely next words from there'''
        sentence = [word]
        counter = 0
        while len(sentence) < int(length):
            word = self.predict_word(word)[counter]
            if word in sentence:
                counter += 1
            else:
                counter = 0
            sentence.append(word)
        return ' '.join(sentence)



if __name__ == '__main__':
    translator = TextAnalyzer(sys.argv[1])
    translator.loadWords()
    translator.word_count()
    #print(translator.most_common())
    translator.get_pairs()
    translator.pairs_frequency()
    translator.prediction_dict()
    print(translator.pre_dict[sys.argv[2]])
    print(f"The most likely word to follow '{sys.argv[2]}' is '{translator.predict_word(sys.argv[2])[0]}'")
    print(translator.make_sentence(sys.argv[2], 50))
