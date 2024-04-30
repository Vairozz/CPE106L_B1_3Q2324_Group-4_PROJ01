import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


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
        elif not email.endswith('@gmail.com'):
            messagebox.showerror("Error", "Please enter a valid Gmail address.")
        else:
            messagebox.showinfo("Success", "Account created successfully!")
            page.destroy()
            create_login_page()

    page = tk.Tk()
    page.title('REGISTER')
    page.geometry('500x750')
    page.configure(bg='#000000')
    page.resizable(False, False)

    title_label = ttk.Label(
        page,
        text='BUS SCHEDULER APP',
        font=('Arial', 30, 'bold'),
        foreground='#ffffff',
        background='#000000'
    )
    title_label.place(relx=0.5, rely=0.05, anchor='center')

    info_label = ttk.Label(
        page,
        text='PLEASE ENTER YOUR INFORMATION BELOW \nTO MAKE AN ACCOUNT',
        font=('Arial', 14),
        foreground='#ffffff',
        background='#000000',
        justify=tk.CENTER
    )
    info_label.place(relx=0.5, rely=0.2, anchor='center')

    # Name and Age Labels and Entries in the same row
    name_label = ttk.Label(
        page,
        text='Name:',
        font=('Arial', 14),
        foreground='#ffffff',
        background='#000000'
    )
    name_label.place(relx=0.1, rely=0.3)

    name_entry = ttk.Entry(page, font=('Arial', 14))
    name_entry.place(relx=0.1, rely=0.33, relwidth=0.45, relheight=0.05)

    age_label = ttk.Label(
        page,
        text='Age:',
        font=('Arial', 14),
        foreground='#ffffff',
        background='#000000'
    )
    age_label.place(relx=0.6, rely=0.3)

    age_entry = ttk.Entry(page, font=('Arial', 14))
    age_entry.place(relx=0.6, rely=0.33, relwidth=0.3, relheight=0.05)

    # Address Label and Entry
    address_label = ttk.Label(
        page,
        text='Address:',
        font=('Arial', 14),
        foreground='#ffffff',
        background='#000000'
    )
    address_label.place(relx=0.1, rely=0.4)

    address_entry = ttk.Entry(page, font=('Arial', 14))
    address_entry.place(relx=0.1, rely=0.43, relwidth=0.8, relheight=0.05)

    email_label = ttk.Label(
        page,
        text='Gmail Account',
        font=('Arial', 14),
        foreground='#ffffff',
        background='#000000'
    )
    email_label.place(relx=0.1, rely=0.5)

    email_entry = ttk.Entry(page, font=('Arial', 14))
    email_entry.place(relx=0.1, rely=0.53, relwidth=0.8, relheight=0.05)

    username_label = ttk.Label(
        page,
        text='Username',
        font=('Arial', 14),
        foreground='#ffffff',
        background='#000000'
    )
    username_label.place(relx=0.1, rely=0.6)

    username_entry = ttk.Entry(page, font=('Arial', 14))
    username_entry.place(relx=0.1, rely=0.63, relwidth=0.8, relheight=0.05)

    password_label = ttk.Label(
        page,
        text='Password:',
        font=('Arial', 14),
        foreground='#ffffff',
        background='#000000'
    )
    password_label.place(relx=0.1, rely=0.7)
    password_entry = ttk.Entry(page, font=('Arial', 14), show='*')
    password_entry.place(relx=0.1, rely=0.73, relwidth=0.8, relheight=0.05)

    confirm_label = ttk.Label(
        page,
        text='Confirm Password:',
        font=('Arial', 14),
        foreground='#ffffff',
        background='#000000'
    )
    confirm_label.place(relx=0.1, rely=0.8)

    confirm_entry = ttk.Entry(page, font=('Arial', 14), show='*')
    confirm_entry.place(relx=0.1, rely=0.83, relwidth=0.8, relheight=0.05)

    create_account_button = ttk.Button(
        page,
        text='CREATE ACCOUNT',
        style='Create.TButton',
        command=create_account  # Call the create_account function when the button is clicked
    )
    create_account_button.place(relx=0.5, rely=0.93, relwidth=0.6,  anchor='center')

    style = ttk.Style()
    style.configure('Create.TButton', foreground='#000000', background='#FF0000', borderwidth=0, border_radius=100)
    style.map('Create.TButton', background=[('active', '#FF0000')])

    return page


def create_login_page():
    page = tk.Tk()
    page.title('Login')
    page.geometry('500x750')
    page.configure(bg='#000000')
    page.resizable(False, False)

    title_label = ttk.Label(
        page,
        text='BUS SCHEDULER APP',
        font=('Arial', 30, 'bold'),
        foreground='#ffffff',
        background='#000000'
    )
    title_label.place(relx=0.5, rely=0.05, anchor='center')

    info_label = ttk.Label(
        page,
        text='PLEASE ENTER YOUR INFORMATION BELOW \nTO LOGIN TO YOUR ACCOUNT',
        font=('Arial', 14),
        foreground='#ffffff',
        background='#000000',
        justify=tk.CENTER
    )
    info_label.place(relx=0.5, rely=0.2, anchor='center')

    username_label = ttk.Label(
        page,
        text='Username',
        font=('Arial', 14),
        foreground='#ffffff',
        background='#000000'
    )
    username_label.place(relx=0.1, rely=0.3)

    username_entry = ttk.Entry(page, font=('Arial', 14))
    username_entry.place(relx=0.5, rely=0.35, relwidth=0.8, relheight=0.05, anchor='center')

    password_label = ttk.Label(
        page,
        text='Password',
        font=('Arial', 14),
        foreground='#ffffff',
        background='#000000'
    )
    password_label.place(relx=0.1, rely=0.4)

    password_entry = ttk.Entry(page, font=('Arial', 14), show='*')
    password_entry.place(relx=0.5, rely=0.45, relwidth=0.8, relheight=0.05, anchor='center')

    def login_clicked():
        page.destroy()

    login_button = ttk.Button(
        page,
        text='LOGIN',
        command=login_clicked,
        style='Login.TButton'
    )
    login_button.place(relx=0.5, rely=0.6, relwidth=0.6, relheight=0.08, anchor='center')  # Adjust height for roundness

    create_account_button = ttk.Button(
        page,
        text='CREATE ACCOUNT',
        command=lambda: [page.destroy(), create_register_page()],  # Destroy page before creating register page
        style='Create.TButton'
    )
    create_account_button.place(relx=0.5, rely=0.75, relwidth=0.6, relheight=0.08, anchor='center')  # Adjust height for roundness

    style = ttk.Style()
    style.configure('Login.TButton', foreground='#000000', background='#FF0000', borderwidth=0, border_radius=100)
    style.map('Login.TButton', background=[('active', '#FF0000')])

    style.configure('Create.TButton', foreground='#000000', background='#FF0000', borderwidth=0, border_radius=100)
    style.map('Create.TButton', background=[('active', '#FF0000')])

    page.mainloop()


if __name__ == "__main__":
    create_login_page()
