def striped_words(string):
  '''Takes a string of words, and counts "striped words", which are words that
     alternate vowel and consonant. Single letter words aren't striped.'''

  # create the ref list of vowels
  vowels = set(['A', 'E', 'I', 'O', 'U', 'Y'])
  consonants = set(['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K',
                'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
                'V', 'W', 'X', 'Z'])

  # break the string into individual words by whitespace, punctuation
  words = ""
  for char in string:
    if char == " " or char.isalnum():
        words += char
    else:
        words += " "
  words = words.upper().split()


  # initialize a counter
  striped = 0
  striped_word = []

  # for each word in the string
  for word in words:

    if not len(word) > 1:
        # if word length is one, skip to next word
        continue
    else:
        # group alternating letters together
        odd_letters = set(word[0::2])
        even_letters = set(word[1::2])

        if (odd_letters.issubset(vowels) and even_letters.issubset(consonants)):
          striped += 1
          striped_word.append(word)
        elif (odd_letters.issubset(consonants) and even_letters.issubset(vowels)):
          striped += 1
          striped_word.append(word)
        else:
          pass

  return striped



print(striped_words("My name is ...")) # should be 3
print(striped_words("Hello world")) # 0
print(striped_words("A quantity of striped words.")) # 1
print(striped_words("Dog,cat,mouse,bird.Human.")) # 3
