# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

#imports
import simplegui
import random

num_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global remaining_guesses
    
    if num_range == 100:
        print "New game. Range is [0,100)"
        secret_number = random.randrange(0,100)
        remaining_guesses = 7
        print "Number of remaining guesses is "+str(remaining_guesses)+"\n"
    elif num_range == 1000:
        print "New game. Range is [0,1000)"
        secret_number = random.randrange(0,1000)
        remaining_guesses = 10
        print "Number of remaining guesses is "+str(remaining_guesses)+"\n"
    else:
        print "Error num range "+str(num_range)+" is not correct"


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global remaining_guesses
    print "Guess was "+guess
    remaining_guesses-=1
    print "Number of remaining guesses is "+str(remaining_guesses)
    if remaining_guesses == 0:
        print "You ran out of guesses.  The number was "+str(secret_number)+"\n"
        new_game()
    else:
        guess_num = int(guess)
        if guess_num < secret_number:
            print "Higher!\n"
        elif guess_num > secret_number:
            print "Lower!\n"
        else:
            print "Correct!\n"
            new_game()

    
# create frame
frame = simplegui.create_frame('Frame', 100, 200)
frame.add_input('Input', input_guess, 100)
frame.add_button('Range is [0,100)',range100) 
frame.add_button('Range is [0,1000)',range1000) 
# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
