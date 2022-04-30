import random
import sys

wins = 0
losses = 0
ties = 0

while True:
    print("Wins:", wins, "Losses:", losses, "Ties:", ties)
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")


    choice = input()

    while choice != "r" and choice != "p" and choice != "s" and choice != "q":
        print("Please enter r, p, s, or q")
        choice = input()

    if choice == "r":
        choice = "rock"
    elif choice == "p":
        choice = "paper"
    elif choice == "s":
        choice = "scissors"
    else:
        sys.exit()

    number = random.randint(1, 3)

    if number == 1:
        enemyChoice = "rock"
    elif number == 2:
        enemyChoice = "paper"
    else:
        enemyChoice = "scissors"

    print(choice, "VERSUS", end=" ")
    print(enemyChoice)

    if (choice == "rock" and enemyChoice == "scissors") or (choice == "paper" and enemyChoice == "rock") or (choice == "scissors" and enemyChoice == "paper"):
        print("Win!")
        wins += 1
    elif enemyChoice == choice:
        print("Tie!")
        ties += 1
    else:
        print("Lose!")
        losses += 1
