MOVES = ["rock", "paper", "scissors"]

# Gets the PLAYers names.
P1_NAME = input("What's PLAYer 1's name? ")
P2_NAME = input("What's PLAYer 2's name? ")

# Users tell if they want to PLAY.
PLAY = input("Would you like to PLAY rock, paper, scissors? yes/no ")

# If the Players want to PLAY the code is executed.
if PLAY == "yes":

    # Gets the PLAYer 1 move choice
    P1CHOICE = input("What's PLAYer 1's choice? ")

    #Seperates PLAYer 1's choice from PLAYer 2's choice with 150 LINES
    for X in range(150):
        print("")

    # Gets the PLAYer 2 move choice
    P2_CHOICE = input("What's PLAYer 2's choice? ")

    # Checks to see if MOVES are allowed
    if P1CHOICE not in MOVES or P2_CHOICE not in MOVES:
        print("Improper choice(s)!")

    # Determines the outcome
    # Tie outcomes
    if P1CHOICE == P2_CHOICE and P1CHOICE != "rock":
        print("It's a tie!")
    elif P1CHOICE == P2_CHOICE and P1CHOICE == "rock":
        print("You both lose!")

    # P1 wins outcomes
    elif P1CHOICE == "rock" and P2_CHOICE == "scissors":
        print(P1_NAME, "Wins!")
    elif P1CHOICE == "paper" and P2_CHOICE == "rock":
        print(P1_NAME, "Wins!")
    elif P1CHOICE == "scissors" and P2_CHOICE == "paper":
        print(P1_NAME, "Wins!")

    # P2 win outcoms
    elif P1CHOICE == "scissors" and P2_CHOICE == "rock":
        print(P2_NAME, "Wins!")
    elif P1CHOICE == "rock" and P2_CHOICE == "paper":
        print(P2_NAME, "Wins!")
    elif P1CHOICE == "paper" and P2_CHOICE == "scissors":
        print(P2_NAME, "Wins!")

# If the players don't want to play is says goodbye
elif PLAY == "no":
    print("Goodbye!")
