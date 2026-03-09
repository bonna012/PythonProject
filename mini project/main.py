import random
def play_game():
    secret = random.randint(1,100)
    attempts = 0
    print("Guess the number between 1 to 100")
    while True:
        guess_input = input("Enter your guess:")
        if not guess_input.isdigit():
            print("Please enter a valid number.")
            continue
        guess_input = int(guess_input)
        attempts += 1
        if guess_input < 1 or guess_input > 100:
            print("Please guess a number between 1 and 100.") 
            continue
        elif guess_input < secret:
         print("Too low! Try again.")
        elif guess_input > secret:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break
        print()
if __name__ == "__main__":   
    main()
