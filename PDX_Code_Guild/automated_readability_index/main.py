#TODO

            # Print the following to console

            # --------------------------------------------------------

            # The ARI for the file, {filename}, is {ARI score}.
            # This corresponds to a {grade-level} level of difficulty
            # that is suitable for an average person of {ages} years old.

            # --------------------------------------------------------

    # Any scores > 14 should be treated as ARI_score of 14.

from math import ceil
import nltk
import subprocess as sp

class ReadabilityIndexer:
    '''Used to instantiate an object that will parse text, calculate its level of reading difficulty,
    and inform a user. '''

    def __init__(self):
        self.ari_scale = {
         1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
         2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
         3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
         4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
         5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
         6: {'ages': '10-11', 'grade_level':    '5th Grade'},
         7: {'ages': '11-12', 'grade_level':    '6th Grade'},
         8: {'ages': '12-13', 'grade_level':    '7th Grade'},
         9: {'ages': '13-14', 'grade_level':    '8th Grade'},
        10: {'ages': '14-15', 'grade_level':    '9th Grade'},
        11: {'ages': '15-16', 'grade_level':   '10th Grade'},
        12: {'ages': '16-17', 'grade_level':   '11th Grade'},
        13: {'ages': '17-18', 'grade_level':   '12th Grade'},
        14: {'ages': '18-22', 'grade_level':      'College'}
    }
        self.sentence_count = 0
        self.word_count = 0
        self.char_count = 0

        self.menu =  {1: "geneology-of-morals.txt",
                      2: "gettysburg-address.txt",
                      3: "jack-and-jill.txt",
                      'q': "Quit"
                      }

    def display_menu(self):
        for key in self.menu:
            print(f"{key}:  {self.menu[key]}")

    def parse_text(self, text):
        '''Parses given text, returns number of sentences, words, and chars.'''
        # Create sentence array
        with open(text) as raw_text:
            text = raw_text.read()
            self.sentence_count = len(nltk.sent_tokenize(text))
            self.word_count = len(nltk.word_tokenize(text))
            self.char_count = len("".join(text.split()))


    def calc_ari(self):
        '''Returns the ARI score for a given text's number of sentences, words, chars.
        Takes three ints, outputs an int.'''

        ari_score = ceil(4.71 * (self.char_count / self.word_count) + 0.5 * (self.word_count / self.sentence_count) - 21.43)
        if ari_score > 14:
            ari_score = 14
        return ari_score

    def display_ari(self, score, to_read):
        '''Prints out the results of readability analysis'''
        sp.call('clear', shell=True)
        print(f'''
        --------------------------------------------------------

        The ARI for the file, {to_read}, is {score}.
        This corresponds to a {self.ari_scale[score]['grade_level']} level of difficulty
        that is suitable for an average person of {self.ari_scale[score]['ages']} years old.

        --------------------------------------------------------''')
        print()

if __name__ == '__main__':
    ari = ReadabilityIndexer()
    while True:
        print()
        ari.display_menu()
        text = input("Enter the number of the text you'd like to analyze: ")
        if text == 'q':
            exit()
        else:
            to_read = ari.menu[int(text)]
            ari.parse_text(to_read)
            score = ari.calc_ari()
            ari.display_ari(score, to_read)





