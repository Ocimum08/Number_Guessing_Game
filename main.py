import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    # Randomly select a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        # Take user input
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Provide feedback based on the user's guess
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            
number_guessing_game()
