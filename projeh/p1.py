import sqlite3
import tkinter as tk
from tkinter import messagebox


# connect to database
conn = sqlite3.connect('atm.db')


# create a table for users
conn.execute(''' CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY, 
          username TEXT NOT NULL ,
          password TEXT NOT NULL, 
          balance REAL NOT NULL DEFAULT 0
          )'''
          )

conn.commit()

# functionals about atm work
def chek_balance(username):
    """برای بررسی کردن موجودی حساب بانکی"""

    conn.execute("SELECT balance FROM users WHERE username=?", (username,))
    return conn.fetchone()[0]

def deposit(username, amount):
    """برای واریز پول به حساب """

    conn.execute("UPDATE users  SET balance = balance + ? WHERE username=?", (amount, username))
    conn.commit()

def withdraw(username, amount):
    """برای برداشت از حساب"""

    conn.execute("SELECT balance FROM users WHERE username=?", (username))
    balance = conn.fetchone()[0]
    if amount > balance:
        return False
    else:
        conn.execute("UPDATE users SET balance = balance - ? WHERE username=?", (amount, username))
        conn.commit()
        return True
    
def register_user(username, password):
    """برای ایجاد حساب بانکی"""

    try:
        conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("New User", "Registration was successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Username", "It is repetitive")

# create atm with tkinter 
def Atm_interface():
    """اینجا قیافه کار رو در میاریم"""
    def login():
        username = entry_username.get()
        password = entry_password.get()
        conn.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = conn.fetchone()
        if user:
            main_menu(user[1])
        else:
            messagebox.showerror("Name", "Username or password is not correct!")
    
    def register():
        username = entry_username.get()
        password = entry_password.get()
        register_user(username, password)


    def atm():
        global entry_username, entry_password
        window = tk.Tk()
        window.title("ATM APP")
        window.geometry("300x300")
        window.bg("dark blue")

        label1 = tk.Label(window, text="Username:", font=("Hack", 20, "bold"), bg="light green")
        label1.pack()
        entry_username = tk.Entry(window)
        entry_username.pack()

        label2 = tk.Label(window, text= "Password")
        label2.pack()
        entry_password = tk.Event(window)
        entry_password.pack()

        btn1 = tk.Button(window, text= "Login", command= login)
        btn1.pack()

        btn2 = tk.Button(window, text= "Register", command= register)
        btn2.pack()

        window.mainloop()

def main_menu(username):
    root = tk.Tk()
    root.title("Main menu")

    def view_balance():
        balance = chek_balance(username)
        messagebox.showinfo(f"Your balance :", {balance}, "IRR")

    def diposit_mony():
        amount =float(entry_amount.get())
        deposit(username, amount)
        messagebox.showinfo({amount}, f"IRR Credited to your account.")
    
    def withdrw_money():
        amount =float(entry_amount.get())
        if withdraw(username, amount):
            messagebox.showinfo({amount}, f"IRR DEdcuted from your account.")
        else:
            messagebox.showerror("Warning", "Your balance is not enough!")

    def atM():
        global entry_amount
        label3 = tk.Label(root, text= "Amount")
        label3.pack()
        entry_amount = tk.Entry(root)
        entry_amount.pack()

        btn3 = tk.Button(root, text= "View balance", command= view_balance)
        btn3.pack()

        btn4 = tk.Button(root, text= "Deposit money", command= diposit_mony)
        btn4.pack()

        btn5 = tk.Button(root, text= "Withdraw money", command= withdrw_money)
        btn5.pack()

        root.mainloop()

if __name__ == "__main__":
    Atm_interface()
