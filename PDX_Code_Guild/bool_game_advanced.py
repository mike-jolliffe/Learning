"""
PDX Code Guild Curriculum. Boolean Game.
"""

import random

class BasicGame():
    '''Create class for running a basic game of simple boolean expressions'''
    bools = {
            'not False': not False,
            'not True': not True,
            'True or False': True or False,
            'True or True': True or True,
            'False or True': False or True,
            'False or False': False or False,
            'True and False': True and False,
            'True and True': True and True,
            'False and True': False and True,
            'False and False': False and False,
            'not (True or False)': not (True or False),
            'not (True or True)': not (True or True),
            'not (False or True)': not (False or True),
            'not (False or False)': not (False or False),
            'not (True and False)': not (True and False),
            'not (True and True)': not (True and True),
            'not (False and True)': not (False and True),
            'not (False and False)': not (False and False),
            '1 != 0': 1 != 0,
            '1 != 1': 1 != 1,
            '0 != 1': 0 != 1,
            '0 != 0': 0 != 0,
            '1 == 0': 1 == 0,
            '1 == 1': 1 == 1,
            '0 == 1': 0 == 1,
            '0 == 0': 0 == 0,
            }


    def random_question(self):
        question = random.choice(list(self.bools.keys()))
        answer = self.bools[question]

        return question, answer

    def run(self):
        score = 0
        print('Welcome to the boolean value game!')
        print('Type (T)rue or (F)alse for each question.')

        while len(self.bools) > 0:
            left = len(self.bools)
            print("You have answered {score} of 26 questions correctly.".format(score=str(score)))
            print("There are {left} questions left.".format(left=str(left)))
            question = self.random_question()
            player_answer = input("What is the value of {q}?: ".format(q=question[0]))

            if player_answer.lower() == "t":
                player_answer = 'True'
            elif player_answer.lower() == 'f':
                player_answer = 'False'

            if player_answer == str(question[1]):
                print("********** That is correct! **********")
                #TODO resolve the following statement that's commented out
                if len(question) == 2:
                    self.bools.pop(question[0])
                else:
                    self.bools.pop(question[2])
                score += 1
            else:
                print("Sorry, that is not correct.")

class AdvancedGame(BasicGame):
    '''Build a class that inherits from BasicGame, but concatenates two of the
    BasicGame questions into a single, more complicated boolean expression'''

    bools_connector = ["and", "or"]

    def __init__(self):
        BasicGame.__init__(self)

    def random_question(self):
        question1 = random.choice(list(self.bools.keys()))
        answer = self.bools[question1]

        question2 = random.choice(list(self.bools.keys()))
        answer2 = self.bools[question2]

        connector = random.choice(self.bools_connector)
        advanced_ans = f"{answer} {connector} {answer2}"
        return f"{question1} {connector} {question2}", eval(advanced_ans), question1

if __name__ == "__main__":
    difficulty = input("Pick a difficulty: Beginner or Advanced? ")
    if difficulty in ["B", "Beginner", "b", "beginner"]:
        game = BasicGame()
    else:
        game = AdvancedGame()
    game.run()
