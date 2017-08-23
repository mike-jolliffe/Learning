import random

# Get user input
user_input = input("Give me three comma-separated adjectives: ")

def madlib_builder(user_input):
    # Split user input into an array of three elements
    adj_array = user_input.split()
    # Using random.shuffle(), insert the three adjectives into the story
    random.shuffle(adj_array)
    # Print the result as a silly formatted string back to the console
    print("At the zoo, I saw a {} giraffe, a {} penguin, and a {} zebra".format(adj_array[0],
        adj_array[1], adj_array[2]))
# Call the function on the user's input, so when file is executed, function is called
madlib_builder(user_input)
