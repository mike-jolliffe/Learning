from random import randint

def roll(num_dice, sides):
    '''returns pseudo-random rolls of an arbitrary number of dice with an arbitrary number of sides'''
    results = []

    for die in range(num_dice):
        results.append(randint(1,sides))

    return results


print(*(roll(5, 20)))

