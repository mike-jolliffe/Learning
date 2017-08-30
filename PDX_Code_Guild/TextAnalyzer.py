import string
import codecs
#open it with utf-8 encoding
#f=codecs.open("myfile.txt","r",encoding='utf-8')
#read the file to unicode string
#sfile=f.read()

#check the encoding type
#print type(file) #it's unicode

#unicode should be encoded to standard string to display it properly
#print sfile.encode('utf-8')
#check the type of encoded string

#print type(sfile.encode('utf-8'))

class TextAnalyzer():
    '''
    
    Count how often each unique pair of words is used, then print the most frequent top 10 out with their counts.

    Make a command line tool with the `sys.argv`.Allow the the user to pass in the filename to a `.txt` file when execiting your program.Use the
    `sys.argv` to parse the filename to use for the analysis.

    Allow the user to enter a word and get the most likely words to follow the given word. Store the pair counts as a dict
    of dicts, where the first key is the first word in the pair and the second key is the second word.

    EX: Enter Query Word > Mr.
        The most likely bi - gram pair starting
        with "Mr." is "Mr. Darcy".


    Redo the pair counts: normalize the probabilities in the inner dict by the count of pairs that start with the first word.

    Chain together that ability to generate random sentences, one word at a time, from a given starting word.'''

    def __init__(self, input_file):
        self.input_file = (open(input_file)).read()
        self.words_array = []
        self.count = {}

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
        most_freq = [(k, self.count[k]) for k in sorted(self.count, key=self.count.get, reverse=True)]
        return most_freq[:11]



translator = TextAnalyzer("alice2.txt")
translator.loadWords()
translator.word_count()
print(translator.most_common())
