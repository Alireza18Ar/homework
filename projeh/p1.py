import sqlite3
import tkinter as tk
from tkinter import messagebox

# connect to database
conn = sqlite3.connect('atm.db')

# create a table for users
conn.execute(''' CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY, 
          username TEXT NOT NULL UNIQUE,
          password TEXT NOT NULL, 
          balance REAL NOT NULL DEFAULT 0
          )'''
          )

conn.commit()

# functionals about atm work
def check_balance(username):
    """Check the account balance."""
    cursor = conn.execute("SELECT balance FROM users WHERE username=?", (username,))
    return cursor.fetchone()[0]

def deposit(username, amount):
    """Deposit money into the account."""
    conn.execute("UPDATE users SET balance = balance + ? WHERE username=?", (amount, username))
    conn.commit()

def withdraw(username, amount):
    """Withdraw money from the account."""
    cursor = conn.execute("SELECT balance FROM users WHERE username=?", (username,))
    balance = cursor.fetchone()[0]
    if amount > balance:
        return False
    else:
        conn.execute("UPDATE users SET balance = balance - ? WHERE username=?", (amount, username))
        conn.commit()
        return True
    
def register_user(username, password):
    """Create a bank account."""
    try:
        conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("New User", "Registration was successful!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Username", "Username already exists.")

# create atm with tkinter 
def atm_interface():
    """Create the ATM interface."""
    def login():
        username = entry_username.get()
        password = entry_password.get()
        cursor = conn.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        if user:
            main_menu(user[1])
        else:
            messagebox.showerror("Error", "Username or password is incorrect!")

    def register():
        username = entry_username.get()
        password = entry_password.get()
        register_user(username, password)

    window = tk.Tk()
    window.title("ATM APP")
    window.geometry("300x300")
    window.configure(bg="dark blue")

    label1 = tk.Label(window, text="Username:", font=("Hack", 20, "bold"), bg="light green")
    label1.pack()
    entry_username = tk.Entry(window)
    entry_username.pack()

    label2 = tk.Label(window, text="Password:")
    label2.pack()
    entry_password = tk.Entry(window, show='*')  # Correct password entry
    entry_password.pack()

    btn1 = tk.Button(window, text="Login", command=login)
    btn1.pack()

    btn2 = tk.Button(window, text="Register", command=register)
    btn2.pack()

    window.mainloop()

def main_menu(username):
    root = tk.Tk()
    root.title("Main Menu")

    def view_balance():
        balance = check_balance(username)
        messagebox.showinfo("Your Balance", f"{balance} IRR")

    def deposit_money():
        try:
            amount = float(entry_amount.get())
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            deposit(username, amount)
            messagebox.showinfo("Success", f"{amount} IRR credited to your account.")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def withdraw_money():
        try:
            amount = float(entry_amount.get())
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            if withdraw(username, amount):
                messagebox.showinfo("Success", f"{amount} IRR deducted from your account.")
            else:
                messagebox.showerror("Warning", "Insufficient funds!")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    label3 = tk.Label(root, text="Amount:")
    label3.pack()
    entry_amount = tk.Entry(root)
    entry_amount.pack()

    btn3 = tk.Button(root, text="View Balance", command=view_balance)
    btn3.pack()

    btn4 = tk.Button(root, text="Deposit Money", command=deposit_money)
    btn4.pack()

    btn5 = tk.Button(root, text="Withdraw Money", command=withdraw_money)
    btn5.pack()

    root.mainloop()

if __name__ == "__main__":
    atm_interface()
