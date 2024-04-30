import tkinter as tk
from tkinter import ttk
from Register import create_register_page  # Import the function from register.py

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

    return page

if __name__ == "__main__":
    login_page = create_login_page()
    login_page.mainloop()
