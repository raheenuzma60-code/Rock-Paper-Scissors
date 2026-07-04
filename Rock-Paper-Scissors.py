import random

choices = ["Rock", "Paper", "Scissors"]

play_again = "y"

while play_again.lower() == "y":

    print("\nChoose an option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user = int(input("Enter your choice (1-3): "))

    if user < 1 or user > 3:
        print("Invalid choice! Please enter a number between 1 and 3.")
        continue

    computer = random.randint(1, 3)

    print("You chose:", choices[user - 1])
    print("Computer chose:", choices[computer - 1])

    if user == computer:
        print("🤝 It's a Draw!")

    elif ((user == 1 and computer == 3) or
          (user == 2 and computer == 1) or
          (user == 3 and computer == 2)):
        print("🎉 You Win!")

    else:
        print("💻 Computer Wins!")

    play_again = input("\nDo you want to play again? (y/n): ")

print("Thanks for playing!")
