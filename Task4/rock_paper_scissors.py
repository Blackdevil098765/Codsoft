import random

def play_game():
    # Initialize scores
    user_score = 0
    computer_score = 0
    options = ["rock", "paper", "scissors"]

    print("--- Welcome to Rock-Paper-Scissors! ---")
    print("Instructions: Type your choice. First to win the round gets a point.")

    while True:
        # 1. User Input
        user_choice = input("\nChoose rock, paper, or scissors (or 'exit' to quit): ").lower()
        
        if user_choice == 'exit':
            break
        
        if user_choice not in options:
            print("Invalid input! Please try again.")
            continue

        # 2. Computer Selection
        computer_choice = random.choice(options)

        # 3. Display Choices
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # 4. Game Logic & Result
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round!")
            user_score += 1
        else:
            print("You lose this round!")
            computer_score += 1

        # 5. Score Tracking (Optional Task)
        print(f"Current Score -> You: {user_score} | Computer: {computer_score}")

        # 6. Play Again
        play_again = input("Play another round? (y/n): ").lower()
        if play_again != 'y':
            break

    print("\n--- Final Game Summary ---")
    print(f"Final Score - You: {user_score} | Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
