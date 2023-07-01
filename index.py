import random

# generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# set the number of guesses allowed
num_guesses = 3

# loop through the guesses
for guess_num in range(num_guesses):
    # get the user's guess
    guess = int(input("Guess a number between 1 and 10: "))

    # check if the guess is correct
    if guess == secret_number:
        print("Congratulations, you guessed it!")
    
        # if the guess is incorrect, let the user know
        print("Sorry, that's not it.")
        # let the user know how many guesses are left
        guesses_left = num_guesses - guess_num - 1
        print(f"You have {guesses_left} guesses left.")

# if the user runs out of guesses, let them know the secret number
if guess != secret_number:
    print(f"Sorry, you're out of guesses. The secret number was {secret_number}.")
