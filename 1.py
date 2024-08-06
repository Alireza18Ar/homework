player = 0
computer = 0 
choices = ["rock", "paper", "scissor"]

for i in range(5):
    player1 = input("enter your choice: ")
    import random
    player2 = random.choice(choices)
    print(f"computer: {player2}")

    if player1 == player2:
        print("draw")
    elif player2 == "rock" and player1 == "paper":
        print("player1 win")
        player += 1
    elif player2 == "rock" and player1 == "scissor":
        print("player2 win")
        computer += 1
    elif player2 == "paper" and player1 == "rock":
        print("player2 win")
        computer += 1 
    elif player2 == "paper" and player1 == "scissor":
        print("player1 win")
        player += 1 
    elif player2 == "scissor" and player1 == "rock":
        print("player1 win")
        player += 1 
    elif player2 == "scissor" and player1 == "paper":
        print("player2 win")
        computer += 1          
    else: 
        print("invalid input")


if player > computer:
    print(f"player1 win with {player} score")
elif player < computer:
    print(f"player2 win with {computer} score")
else:
    print("draw")