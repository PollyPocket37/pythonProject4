import random  # bring in the random number
import time

number = random.randint(1, 200)  # pick the number between 1 and 200


def intro():

    print("We are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(.5)
    print("Go ahead. Guess!")

    intro()


def pick():
        enter = input("Guess: ")  # inserts the place to enter guess
        try:  # check if a number was entered
            guess = int(enter)  # stores the guess as an integer instead of a string

            if guess <= 200 and guess >= 1:
                    if guess < number:
                        print("That's too low")
                    if guess > number:
                        print("That's too high")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again!")
                    if guess == number:
                        print('Good job! You guessed my number ')
                    if guess != number:
                        print('Nope. The number I was thinking of was ' + str(number))


            if guess > 200 or guess < 1:  # if they aren't in the range
                print("That number isn't in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 200")

        except:  # if a number wasn't entered
            print("I don't think that " + enter + " is a number. Sorry")

pick()

