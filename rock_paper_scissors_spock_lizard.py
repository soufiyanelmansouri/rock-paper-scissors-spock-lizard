import random

choices =["rock", "paper", "scissors", "lizard", "spock"]

user_wins_counter = 0
computer_wins_counter = 0

while True:
    user_input = input("Type rock, paper, scissors, lizard, spock or q to quit: ").lower()
    
    if user_input == "q":
        break
    
    elif user_input not in choices:
        continue
    
    # time for the computer to pick
    random_number = random.randint(0, 4)    
    computer_pick = choices[random_number]
    print(f"the cp choose {computer_pick}")
    
    if user_input == computer_pick:
        print("Draw")
        continue
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win")
        user_wins_counter += 1
    # paper covers rock
    elif user_input == "paper" and computer_pick == "rock":
        print("You win")
        user_wins_counter += 1
    # rock crushes lizard
    elif user_input == "rock" and computer_pick == "lizard":
        print("You win")
        user_wins_counter += 1
    # lizard poisons spock
    elif user_input == "lizard" and computer_pick == "spock":
        print("You win")
        user_wins_counter += 1
    # spock smashes scissors
    elif user_input == "spock" and computer_pick == "scissors":
        print("You win")
        user_wins_counter += 1
    # scissors decapitates lizard
    elif user_input == "scissors" and computer_pick == "lizard":
        print("You win")
        user_wins_counter += 1
    # lizard eats paper
    elif user_input == "lizard" and computer_pick == "paper":
        print("You win")
        user_wins_counter += 1
    # paper disproves spock
    elif user_input == "paper" and computer_pick == "spock":
        print("You win")
        user_wins_counter += 1
    # spock vaporizes rock
    elif user_input == "spock" and computer_pick == "rock":
        print("You win")
        user_wins_counter += 1
    # (and as it always has) rock crushes scissors
    elif user_input == "rock" and computer_pick == "scissors" :    
        print("You won")
        user_wins_counter += 1    
    else:
        print("The computer won")
        computer_wins_counter += 1
        
if computer_wins_counter == user_wins_counter:
    print("Tie!")
else:    
    print(f"You won {user_wins_counter} times")      
    print(f"The computer won {computer_wins_counter} times")    