import sqlite3
import tkinter as tk
from tkinter import messagebox

class Store:
    """ایجاد جدول محصولات پایگاه داده، افزودن محصول جدید، بازگشت لیست تمام محصولات موجود، بستن پایگاه داده"""
    def __init__(self, dbname='STORE'):
        self.con = sqlite3.connect(dbname)
        self.cursor = self.con.cursor()
        self.Creattable()     


    def Creattable(self):
        """ایجاد جدول محصولات پایگاه داده
        """
        self.cursor.execute('''
        CREAT TABLE IF NOT EXECUTE products ( id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL, 
                            price INTEGER NOTNULL )
                                ''')
        self.con.commit()

    def add(self, name, price):
        """افزودن محصول جدید"""
        self.cursor.execute('INSERT INTO prodocts (name, price) VALUES (?, ?)', (name, price))
        self.con.commit()

    def view(self):
        """بازگشت لیست تمام محصولات موجود
        """
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()
    
    def close(self):
        """بستن پایگاه داده
        """
        self.con.close()

class StoreApp:
    """گرافیکی کردن سیستم فروشگاه
    """
    def __init__(self, root):
        self.store = Store()
        self.root = root
        self.root.title("Store System")

        # فریم اضافه کردن محصول جدید
        self.addframe = tk.Frame(self.root)
        self.addframe.pack(pady=10)

        label1 = tk.Label(self.addframe, text="Product Name: ")
        label1.grid(row= 0, column= 0)

        self.productname = tk.Entry(self.addframe)
        self.productname.grid(row= 0, column= 1)

        label2 = tk.Label(self.addframe, text="Price: ")
        label2.grid(row= 1, column= 0)

        self.price = tk.Entry(self.addframe)
        self.price.grid(row= 1, column= 1)

        self.addbtn = tk.Button(self.addframe, text= "Add Product", command= self.addproduct)
        self.addbtn.grid(row= 3, columnspan= 2)

        # دکمه ای برای نشان دادن تمام محصولات موجود
        self.viewbtn = tk.Button(self.root, text= "View Inventory", command= self.view)
        self.viewbtn.pack(pady= 10)

        def addproduct(self):
            name = self.productname.get()
            price = float(self.price.get())

            if name and price >= 0 :
                self.store.addproduct(name, price)
                m = messagebox.showinfo("Success", f'product"{name}" added successfully')
                self.productname.delete(0, tk.END)
                self.price.delete(0, tk.END)

            else:
                messagebox.showerror("Error", "Please enter valid product details.")

        def view(self):
            inventory = self.store.view()
            inwindow = tk.Tk(self.root)
            inwindow.title("Inventory")

            for product in inventory:
                label3 = tk.Label(inwindow, text= f'ID: {product[0]}, Name: {product[1]}, Price: {product[2]}')
                label3.pack()


        def close(self):
            self.store.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = StoreApp(root) 


    root.mainloop()