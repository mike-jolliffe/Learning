import random

def madlib_builder(user_input):
    '''Prints a madlib that formats a string to include user-inputted adjectives'''

    # Split user input into an array of three elements
    adj_array = user_input.split(", ")
    # Using random.shuffle(), insert the three adjectives into the story
    random.shuffle(adj_array)
    return adj_array

def madlib_printer(array):
    # Print the result as a silly formatted string back to the console
    print("At the zoo, I saw a {} giraffe, a {} penguin, and a {} zebra".format(array[0],
        array[1], array[2]))

# Get user input
user_input = input("Give me three comma-separated adjectives: ")

# Call the function on the user's input
madlib_printer(madlib_builder(user_input))
