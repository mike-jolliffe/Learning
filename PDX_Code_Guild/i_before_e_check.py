class CheckIt():
    '''Creates an object that checks if input word follows '"i" before "e", except after "c"' rules'''

    dict = (open("words.txt", "r")).read()

    def __init__(self, word):
        self.word = word

    def check_word(self):
        str1 = "ie"
        str2 = "cie"
        str3 = "ei"
        str4 = "cei"

        if self.word.find(str1):
            if self.word.find(str2):
                # check for errors
                if self.word in self.dict:
                    return True
                else:
                    return False
            else:
                #follows rules
                return True
        elif self.word.find(str3):
            if self.word.find(str4):
                # follows rules
                return True
            else:
                # check for error
                if self.word in self.dict:
                    return True
                else:
                    return False
        else:
            return f"no occurrences in string"

checker = CheckIt("science")
print(checker.check_word())