import random

user_wins=0
comp_wins=0
options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Type Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissor = 2.
    comp_picks = options[random_number]
    print("Computer Picked",comp_picks + ".")

    if user_input == "rock" and comp_picks == "scissor":
        print("You won!!!!!")
        user_wins += 1
        

    elif user_input == "paper" and comp_picks == "rock":
        print("You won!!!!!")
        user_wins += 1
        

    elif user_input == "scissor" and comp_picks == "paper":
        print("You won!!!!!")
        user_wins += 1
        
    else:
        print("You lost :(....")
        comp_wins += 1
print("You won", user_wins, "times.")
print("The computer won", comp_wins, "times.")
    
print("GoodBye.....")