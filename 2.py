import tkinter as tk
import random  

# A function to start the game 
def start():
    user_choice = choice.get()
    options = ["Rock", "scissor", "Paper"]
    computer_choice = random.choice(options)
    result = ""
    
    if user_choice == computer_choice:
        result = "Draw"
    elif (user_choice == "Rock" and computer_choice == "scissor") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "scissor" and computer_choice == "Paper"):
        result = "You Win"
    else:
        result = "Computer Win"

    result_label.config(text=f"Your Choice:{user_choice}\n Computer's Choice:{computer_choice}\n result:{result}")

    
# Making the face of the game 
root =tk.Tk()
root.title("RSP Game")

# Variable to save user selction 
choice = tk.StringVar(value="Rock")

# Create Radiobuttons
Rock_radio = tk.Radiobutton(root, text="Rock", variable=choice, value="Rock", 
font=("arial", 14))
Rock_radio.pack()

Paper_radio = tk.Radiobutton(root, text = "Paper", variable=choice, value="Paper", 
font = ("arial", 14))
Paper_radio.pack()

scissor_radio = tk.Radiobutton(root, text = "scissor", variable=choice, value="scissor", 
font = ("arial", 14))
scissor_radio.pack()

# A button for play
def btnClick(play):
    global play_button
    play_button = (play) + (play)
play_button = tk.Button(root,  text = "Play", command=lambda:btnClick("play"), font=("arial", 16))
play_button.pack(pady=20)

# A stuck for show result
result_label = tk.Label(root, text ='', font= ("arial", 24))
result_label.pack(pady=20)

root.mainloop()



