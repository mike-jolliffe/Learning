number = raw_input("Please think of a number between 0 and 100!")
low = 0
high = 100
x = 50
while True:
    print("Is your secret number {}?".format(x))
    feedback = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if not (feedback == 'h' or feedback == 'l' or feedback == 'c'):
        print ("Sorry, I did not understand your input.")
    elif feedback == 'h':
        high = x
        x = (low+high)/2
    elif feedback == 'l':
        low = x
        x = (low+high)/2
    else:
        break
