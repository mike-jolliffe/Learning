import random
from madlib import madlib_builder, madlib_printer

class MadlibGame(object):

    def __init__(self, libs):
        self.libs = libs

    def run(self):
        array = madlib_builder(self.libs)
        while True:
            madlib_printer(array)
            ask = input("Would you like to hear the story again? ")
            if ask == "no":
                break

libs = input("Please give me three adjectives: ")
new_game = MadlibGame(libs)
new_game.run()
