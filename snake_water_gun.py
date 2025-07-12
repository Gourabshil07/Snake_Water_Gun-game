
import random

dict = {1: "Snake", 2: "Water", 3: "Gun"}

options= [1,2,3]

def random_num():
    
    return random.choice(options)

game=("\n Welcome to the Snake 🐍, Water 💧, Gun 🔫 Game\n")
print(game)

user_score =0
computer_score=0

while True:

    choice = int(input("\nEnter number (1 for Snake, 2 for Water,  3 for Gun): "))

    computer = random_num()

    if choice not in options:
        print("Invalid!")
    else:
        print(f"You choose:{dict[choice]}")
        print(f"Computer choose:{dict[computer]}")
        if choice == computer:
            print("Draw Match 🔴🔴")

    # elif choice == 1 and computer == 2:
    #     print("You Win")
    # elif choice == 1 and computer == 3:
    #     print("Computer Win")
    # elif choice == 2 and computer == 3:
    #     print("You win")
    # elif choice ==2 and computer== 1:
    #     print("Computer win")
    # elif choice ==3 and computer == 1:
    #     print("You Win")
    # elif choice == 3 and computer == 2:
    #     print("Computer Win")

        elif    (choice == 1 and computer ==2) or\
                (choice ==2 and computer==3) or\
                (choice == 3 and computer ==1):
                print("Congratulate🎉 You Win!")
                user_score +=1 # increase user score
        else:
                print("💻 Computer Wins!")
                computer_score += 1 # increase computer score

    print(f"Your Score:{user_score} | Computer Score:{computer_score}\n")
    

    play_again = input("Do you play again? (Y/N): ").upper()

    if play_again != "Y":
         print("\nGoodbye")
         break

