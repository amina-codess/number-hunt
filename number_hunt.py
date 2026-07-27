import random
def number_hunt():
    guess = random.randint(1, 100)

    def valid_guess():
        user_input = int(input("Guess a number between 1 and 100: "))
        while user_input < 1 or user_input > 100:
            user_input = int(input("Guess a number between 1 and 100: "))
        return user_input

    attempts = 10
    found = False
    user_input = valid_guess()
    while attempts > 0:

        if user_input > guess:
            print("Too high")
            attempts -= 1
            print("Attempts left are",attempts)
            user_input = valid_guess()

        elif user_input < guess:
            print("Too low")
            attempts -= 1
            print("Attempts left are", attempts)
            user_input = valid_guess()

        elif user_input == guess:
            print("You guessed it right! Congratulations!")
            print("Attempts left are",attempts)
            found = True
            break

    if attempts == 0 and not found:
        print("You did not guess it right!")
        print("The number was", guess)

number_hunt()



