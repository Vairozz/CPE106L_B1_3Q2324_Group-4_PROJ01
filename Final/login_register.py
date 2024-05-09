import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from user_database import cursor, conn  # Importing the database connection
import sqlite3
from newSidebar import create_new_sidebar
from PIL import Image, ImageTk
from admin_menu import create_admin_menu

def create_register_page():
    def create_account():
        name = name_entry.get()
        age = age_entry.get()
        address = address_entry.get()
        email = email_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_entry.get()

        # Check if any field is empty
        if not all([name, age, address, email, username, password, confirm_password]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        if password != confirm_password:
            messagebox.showerror("Error", "Password and Confirm Password do not match!")
            return
        if not email.endswith('@gmail.com'):
            messagebox.showerror("Error", "Please enter a valid Gmail address.")
            return

        try:
            # Insert user data into the database
            cursor.execute('''
                INSERT INTO users (name, age, address, email, username, password)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, age, address, email, username, password))
            conn.commit()

            messagebox.showinfo("Success", "Account created successfully!")
            page.destroy()
            create_login_page()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already taken. Please choose a different username.")

    page = tk.Tk()
    page.title('REGISTER')
    page.geometry('500x750')
    page.configure(bg='#F2F2EB')
    page.resizable(False, False)

    title_label = ttk.Label(
        page,
        text='BusConnect PH',
        font=('Segoe UI Black', 35, 'bold'),
        foreground='#A41F13',
        background='#F2F2EB'
    )
    title_label.place(relx=0.5, rely=0.155, anchor='center')

    info_label = ttk.Label(
        page,
        text='WHERE EVERY JOURNEY BEGINS',
        font=('Century Gothic', 13, 'bold'),
        foreground='#BE9A60',
        background='#F2F2EB',
        justify=tk.CENTER
    )
    info_label.place(relx=0.5, rely=0.2, anchor='center')

    # Name and Age Labels and Entries in the same row
    name_label = ttk.Label(
        page,
        text='Name:',
        font=('Arial', 11),
        foreground='#401B1B',
        background='#F2F2EB'
    )
    name_label.place(relx=0.1, rely=0.32)

    name_entry = ttk.Entry(page, font=('Arial', 10))
    name_entry.place(relx=0.1, rely=0.35, relwidth=0.45, relheight=0.04)

    age_label = ttk.Label(
        page,
        text='Age:',
        font=('Arial', 11),
        foreground='#401B1B',
        background='#F2F2EB'
    )
    age_label.place(relx=0.6, rely=0.32)

    age_entry = ttk.Entry(page, font=('Arial', 10))
    age_entry.place(relx=0.6, rely=0.35, relwidth=0.3, relheight=0.04)

    # Address Label and Entry
    address_label = ttk.Label(
        page,
        text='Address:',
        font=('Arial', 11),
        foreground='#401B1B',
        background='#F2F2EB'
    )
    address_label.place(relx=0.1, rely=0.4)

    address_entry = ttk.Entry(page, font=('Arial', 10))
    address_entry.place(relx=0.1, rely=0.43, relwidth=0.8, relheight=0.04)

    email_label = ttk.Label(
        page,
        text='Gmail Account:',
        font=('Arial', 11),
        foreground='#401B1B',
        background='#F2F2EB'
    )
    email_label.place(relx=0.1, rely=0.48)

    email_entry = ttk.Entry(page, font=('Arial', 10))
    email_entry.place(relx=0.1, rely=0.51, relwidth=0.8, relheight=0.04)

    username_label = ttk.Label(
        page,
        text='Username:',
        font=('Arial', 11),
        foreground='#401B1B',
        background='#F2F2EB'
    )
    username_label.place(relx=0.1, rely=0.56)

    username_entry = ttk.Entry(page, font=('Arial', 10))
    username_entry.place(relx=0.1, rely=0.59, relwidth=0.8, relheight=0.04)

    password_label = ttk.Label(
        page,
        text='Password:',
        font=('Arial', 11),
        foreground='#401B1B',
        background='#F2F2EB'
    )
    password_label.place(relx=0.1, rely=0.64)
    password_entry = ttk.Entry(page, font=('Arial', 10), show='*')
    password_entry.place(relx=0.1, rely=0.67, relwidth=0.8, relheight=0.04)

    confirm_label = ttk.Label(
        page,
        text='Confirm Password:',
        font=('Arial', 11),
        foreground='#401B1B',
        background='#F2F2EB'
    )
    confirm_label.place(relx=0.1, rely=0.72)

    confirm_entry = ttk.Entry(page, font=('Arial', 10), show='*')
    confirm_entry.place(relx=0.1, rely=0.75, relwidth=0.8, relheight=0.04)

    create_account_button = ttk.Button(
        page,
        text='CREATE ACCOUNT',
        style='Create.TButton',
        command=create_account  # Call the create_account function when the button is clicked
    )
    create_account_button.place(relx=0.5, rely=0.85, relwidth=0.35, relheight=0.05, anchor='center')

    style = ttk.Style()
    style.configure('Create.TButton', foreground='#000000', background='#401B1B', borderwidth=0, border_radius=100)
    style.map('Create.TButton', background=[('active', '#401B1B')])

    return page

  # Display the sidebar menu
def create_login_page():

    def login_clicked():
        username = username_entry.get()
        password = password_entry.get()

        # Check if username and password are in the database
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = cursor.fetchone()
        
        if user:
            if username == 'admin' and password == '123':
                messagebox.showinfo("Success", "Admin Login successful!")
                page.destroy()
                create_admin_menu()
            else:
                messagebox.showinfo("Success", "Login successful!")
                page.destroy()
                create_new_sidebar(username)
                # Implement the logic to navigate to the next page after successful login
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    page = tk.Tk()
    page.title('Login')
    page.geometry('500x750')
    page.configure(bg='#F2F2EB')
    page.resizable(False, False)

    # Open and resize the image
    img = Image.open("bus.png")
    img = img.resize((78,90)) # Adjust the size as needed

    # Convert the image for tkinter
    img_tk = ImageTk.PhotoImage(img)

    # Add a label to display the image
    image_label = ttk.Label(page, image=img_tk)
    image_label.image = img_tk  # Keep a reference to avoid garbage collection
    image_label.place(relx=0.5, rely=0.15, anchor='center')

    title_label = ttk.Label(
        page,
        text='BusConnect PH',
        font=('Segoe UI Black', 35, 'bold'),
        foreground='#A41F13',
        background='#F2F2EB'
    )
    title_label.place(relx=0.5, rely=0.255, anchor='center')

    info_label = ttk.Label(
        page,
        text='WHERE EVERY JOURNEY BEGINS',
        font=('Century Gothic', 13, 'bold'),
        foreground='#BE9A60',
        background='#F2F2EB',
        justify=tk.CENTER
    )
    info_label.place(relx=0.5, rely=0.3, anchor='center')

    username_label = ttk.Label(
        page,
        text='Username',
        font=('Arial', 11),
        foreground='#401B1B',
        background='#F2F2EB'
    )
    username_label.place(relx=0.12, rely=0.470)

    username_entry = ttk.Entry(page, font=('Arial', 10))
    username_entry.place(relx=0.57, rely=0.487, relwidth=0.55, relheight=0.04, anchor='center')

    password_label = ttk.Label(
        page,
        text='Password',
        font=('Arial', 11),
        foreground='#401B1B',
        background='#F2F2EB'
    )
    password_label.place(relx=0.12, rely=0.535)

    password_entry = ttk.Entry(page, font=('Arial', 14), show='*')
    password_entry.place(relx=0.57, rely=0.55, relwidth=0.55, relheight=0.04, anchor='center')

    login_button = ttk.Button(
        page,
        text='LOGIN',
        command=login_clicked,
        style='Login.TButton'
    )
    login_button.place(relx=0.5, rely=0.7, relwidth=0.35, relheight=0.05, anchor='center')  # Adjust height for roundness

    create_account_button = ttk.Button(
        page,
        text='CREATE ACCOUNT',
        command=lambda: [page.destroy(), create_register_page()],  # Destroy page before creating register page
        style='Create.TButton'
    )
    create_account_button.place(relx=0.5, rely=0.77, relwidth=0.35, relheight=0.05, anchor='center')

    style = ttk.Style()
    style.configure('Login.TButton', foreground='#000000', background='#401B1B', borderwidth=0, border_radius=0)
    style.map('Login.TButton', background=[('active', '#401B1B')])

    style.configure('Create.TButton', foreground='#000000', background='#401B1B', borderwidth=0, border_radius=100)
    style.map('Create.TButton', background=[('active', '#401B1B')])

    page.mainloop()


if __name__ == "__main__":
    create_login_page()
