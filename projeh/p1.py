import sqlite3 
import tkinter as tk
from tkinter import messagebox

#ایجاد جدول پایگاه داده
conn = sqlite3.connect('shop.db')

# ایجاد جدول محصولات 
conn.execute(''' CREATE TABLE IF NOT EXISTS products (
             id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             price REAL NOT NULL)''')
conn.close()


# اضافه کردن محصول
def add_product():
    name = entry_name.get()
    price = entry_price.get()

    if name and price:
        conn = sqlite3.connect('shop.db')
        conn.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, float(price)))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Product added successfully")
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Please enter both name and price")

# جستجو کردن محصول
def search_product():
    Product_name = entry_name.get()

    conn = sqlite3.connect('shop.db')
    cursor = conn.execute("SELECT * FROM products WHERE name=?",(Product_name,))
    product = cursor.fetchall()
    conn.close()

    if product:
        entry_price.delete(0, tk.END)
        entry_price.insert(0, product[0])
    else:
        messagebox.showwarning("Warning", "Product not found")

# حذف محصول
def delete_product():
    name = entry_name.get()
    
    conn = sqlite3.connect('shop.db')
    conn.execute('DELETE FROM products WHERE name=?', (name,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Product delete successfully")
    clear_entries()
# ویرایش محصولات
def edit_product():
    name = entry_name.get()
    price = entry_price.get()

    if name and price:
        conn = sqlite3.connect('shop.db')
        conn.execute('UPDATE products SET price=? WHERE name= ?', ((float(price)), name)) 
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Product updated successfully")
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Please enter both name and price.")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)


# بستن برنامه 
def close_app():
    root.destroy()


# ساخت گرافیکی برنامه
root = tk.Tk()
root.title("سوپر مارکت مسعود")
root.geometry("300x200")

label1 = tk.Label(root, text="Product price")
label1.grid(row= 1, column= 0)

label2 = tk.Label(root, text= "Product name")
label2.grid(row= 0 , column= 0)

entry_name =tk.Entry(root)
entry_price = tk.Entry(root)

entry_name.grid(row= 0, column= 1)
entry_price.grid(row= 1, column= 1)

add_btn = tk.Button(root, text= "Add product", command=add_product)
add_btn.grid(row= 2, column= 0)

search_btn = tk.Button(root, text= "Search product", command= search_product)
search_btn.grid(row= 2, column= 1)

delete_btn = tk.Button(root, text= "Delete product", command= delete_product)
delete_btn.grid(row= 3, column= 0)

edit_btn = tk.Button(root, text= "Edit product", command= edit_product)
edit_btn.grid(row= 3, column= 1)

close_btn = tk.Button(root, text="Close", command= close_app)
close_btn.grid(row= 4, columnspan= 4)


root.mainloop()