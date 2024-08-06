user_name = input("pleas enter your name: ")


import random 
def guess_number():
    print(f"hello {user_name} welcome to guess number game")


    number = random.randint(1, 10)
    attempts = 5 
    print("you have 5 attempts to guess the secret number")


    for attempt in range(1, attempts + 1):
        guess = int(input("enter your guess: "))
        
        if guess > number:
            print("your guess biger than number")
        elif guess < number:
            print("your guess smaller than number")
        elif guess == number:
            print("you win!")
            break
    else: 
        print("you lose!")


guess_number()
