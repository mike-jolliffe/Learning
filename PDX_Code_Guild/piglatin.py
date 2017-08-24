class PigLatin():
    '''Class that allows conversion of input string to piglatin'''
    def __init__(self, input_string):
        self.input_string = input_string

    def getCapsandPunc(self):
        '''Stores the capitalization and punctuation of user input word'''
        caps = []
        punc = {}
        for i in range(len(self.input_string)):
            if self.input_string[i].isupper():
                caps.append(i)
            elif not self.input_string[i].isalpha():
                punc[i] = self.input_string[i]
        return caps

    def getFirstVowel(self):
        '''Returns the index of the first vowel'''
        vowels = "AEIOUaeiou"
        for i in range(len(self.input_string)):
            if self.input_string[i] in vowels:
                return i

    def piglatinize(self):
        '''converts user input to pig latin while maintaining caps/punc'''
        index = self.getFirstVowel()
        if self.input_string[-1].isalpha():
            if index == 0:
                return self.input_string + "yay"
            else:
                return self.input_string[index:] + self.input_string[:index] + "ay"
        else:
            if index == 0:
                return self.input_string[:-1] + "yay" + self.input_string[-1]
            else:
                return self.input_string[index: -1] + self.input_string[:index] + "ay" + self.input_string[-1]

    def addCaps(self):
        '''adds capitalization back to piglatinized string'''
        capsnpunc = self.getCapsandPunc()
        print(f"Caps and punc {capsnpunc}")
        piglatinized = self.piglatinize().lower()
        piglatinized = list(piglatinized)
        for i in range(len(piglatinized)):
            if i in capsnpunc:
                piglatinized[i] = piglatinized[i].upper()
        piglatinized = ''.join(piglatinized)

        return f"{self.input_string} in Pig Latin is {piglatinized}"

if __name__ == "__main__":
    word = input("Gimme a word: ")
    new_pig = PigLatin(word)
    print(new_pig.addCaps())
