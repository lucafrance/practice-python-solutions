import random as rm

solution = rm.randint(1, 9)

guess = ""
guess_count = 0
while True:
    guess = input("> guess the number:")
    guess_count += 1
    if guess == "exit":
        print("Bye!")
        exit(0)

    guess = int(guess)
    if guess == solution:
        print("You guessed right! Congrats! :)")
        print("It took you {} guesses.".format(guess_count))
        exit(0)
    elif guess < solution:
        print("Think bigger")
    elif guess > solution:
        print("Think smaller")
    else:
        print("This shouldn't have happened :S")
        exit(1)