import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def play_game():
    user_score = 0
    computer_score = 0

    print(" Welcome to Rock-Paper-Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.\n")

    while True:
        user_choice = input("Your choice: ").lower()

        if user_choice == "quit":
            print("\nThanks for playing!")
            print(f"Final Score -> You: {user_score}, Computer: {computer_score}")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("nvalid choice. Please try again.\n")
            continue

        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "win":
            print("ou win this round!")
            user_score += 1
        elif result == "lose":
            print("ou lose this round!")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"Score -> You: {user_score}, Computer: {computer_score}\n")

       
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            print(f"Final Score -> You: {user_score}, Computer: {computer_score}")
            break
        print()
play_game()
        