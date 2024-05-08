import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk
from ticket_functions import create_ticket, is_ticket_unique, ticket_callback
from history_database import history_callback

class ProfileMenu:
    def __init__(self, root, username):
        self.root = root
        self.username = username

    def display(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        label = tk.Label(self.frame, text="Profile Page", font=("Arial", 12))
        label.pack(fill="both", expand=True)

        self.create_profile_form()

    def create_profile_form(self):
        conn = sqlite3.connect('user_database.db')
        cur = conn.cursor()

        # Fetch user's current profile information
        cur.execute("SELECT name, age, address, email FROM users WHERE username=?", (self.username,))
        user_data = cur.fetchone()
        conn.close()

        if user_data:
            name, age, address, email = user_data

            # Display current profile information
            tk.Label(self.frame, text="Name:").pack()
            self.name_entry = tk.Entry(self.frame)
            self.name_entry.insert(0, name)
            self.name_entry.pack()

            tk.Label(self.frame, text="Age:").pack()
            self.age_entry = tk.Entry(self.frame)
            self.age_entry.insert(0, age)
            self.age_entry.pack()

            tk.Label(self.frame, text="Address:").pack()
            self.address_entry = tk.Entry(self.frame)
            self.address_entry.insert(0, address)
            self.address_entry.pack()

            tk.Label(self.frame, text="Email:").pack()
            self.email_entry = tk.Entry(self.frame)
            self.email_entry.insert(0, email)
            self.email_entry.pack()

            tk.Label(self.frame, text="New Password:").pack()
            self.password_entry = tk.Entry(self.frame, show="*")  # Mask the password input
            self.password_entry.pack()

            tk.Label(self.frame, text="Confirm New Password:").pack()
            self.passwordconfirmation_entry = tk.Entry(self.frame, show="*")  # Mask the password input
            self.passwordconfirmation_entry.pack()
            # Button to update profile
            ttk.Button(self.frame, text="Update Profile", command=self.update_profile).pack()
        else:
            messagebox.showerror("Error", "User not found.")

    def update_profile(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        address = self.address_entry.get()
        email = self.email_entry.get()
        new_password = self.password_entry.get()
        confirm_password = self.passwordconfirmation_entry.get()

    # Check if any field is empty
        if not all([name, age, address, email, new_password, confirm_password]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

    # Check if passwords match
        if new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

    # Update user's profile and password in the database
        conn = sqlite3.connect('user_database.db')
        cur = conn.cursor()
        cur.execute("UPDATE users SET name=?, age=?, address=?, email=?, password=? WHERE username=?",
                (name, age, address, email, new_password, self.username))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Profile updated successfully.")



class BusScheduleMenu:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.selected_item = None

    def display(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=15, pady=15)

        tabs = [("JOYBUS Schedule", "joybus_info"),
                ("FARIÑAS Schedule", "fariñas_info"),
                ("PARTAS Schedule", "partas_info")]

        for tab_name, table_name in tabs:
            tab_frame = ttk.Frame(notebook)
            notebook.add(tab_frame, text=tab_name)

            columns = ("Bus Company Name", "Origin", "Destination", "Time", "Bus Type", "Fare")
            table = ttk.Treeview(tab_frame, columns=columns, show="headings", selectmode="extended")
            table.pack(fill="both", expand=True)

            for col in columns:
                table.heading(col, text=col)
                table.column(col, width=100)

            self.fetch_and_display_data(table, table_name)
            self.bind_selection_event(table)

            generate_button = ttk.Button(tab_frame, text="Generate Ticket",
                                         command=lambda t=table: self.generate_ticket(t))
            generate_button.pack()

    def fetch_and_display_data(self, table, table_name):
        conn = sqlite3.connect('106LPROJ.db')
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table_name}")
        schedule_data = cur.fetchall()
        conn.close()

        for row in schedule_data:
            table.insert("", "end", values=row)

    def bind_selection_event(self, table):
        def on_item_select(event):
            item = table.focus()
            if item:
                self.selected_item = table.item(item, "values")
            else:
                self.selected_item = None

        table.bind("<ButtonRelease-1>", on_item_select)

    def generate_ticket(self, table):
        if self.selected_item:
            ticket_length = 8
            ticket = create_ticket(ticket_length)
            while not is_ticket_unique(ticket):
                ticket = create_ticket(ticket_length)

            bus_company, origin, destination, time, bus_type, fare = self.selected_item
            history_callback(self.username, bus_company, origin, destination, time, bus_type, fare)
            ticket_callback(self.username, bus_company, origin, destination, time, bus_type, fare)

        else:
            messagebox.showwarning("No Selection", "Please select a schedule to generate a ticket.")


class TicketsMenu:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

    def display(self):
        self.create_ticket_table()

    def create_ticket_table(self):
        columns = ("Ticket ID", "Bus Company", "Origin", "Destination", "Time", "Bus Type", "Fare")
        table = ttk.Treeview(self.frame, columns=columns, show="headings", selectmode="browse")
        table.pack(fill="both", expand=True)

        self.fetch_and_display_tickets(table)
        self.add_table_headings(table, columns)

    def fetch_and_display_tickets(self, table):
        conn = sqlite3.connect('tickets.db')
        cur = conn.cursor()
        cur.execute(
            "SELECT ticket_id, bus_company, origin, destination, time, bus_type, fare FROM tickets WHERE username=?",
            (self.username,))
        tickets_data = cur.fetchall()
        conn.close()

        for row in tickets_data:
            table.insert("", "end", values=row)

    def add_table_headings(self, table, columns):
        for col in columns:
            table.heading(col, text=col)
            table.column(col, width=100)  # Adjust column width as needed


class NotificationsMenu:
    def __init__(self, root, username):
        self.root = root
        self.username = username

    def display(self):
        conn = sqlite3.connect('notification.db')
        cur = conn.cursor()
        cur.execute("SELECT company_name, notification FROM notifications")
        notifications_data = cur.fetchall()
        conn.close()

        if notifications_data:
            notifications_label = tk.Label(self.root, text="Notifications", font=("Arial", 18))
            notifications_label.pack()

            for company, notification in notifications_data:
                notification_text = f"{company}: {notification}"
                notification_label = tk.Label(self.root, text=notification_text)
                notification_label.pack()
        else:
            no_notifications_label = tk.Label(self.root, text="No notifications available.")
            no_notifications_label.pack()


class HistoryMenu:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

    def display(self):
        self.create_history_table()

    def create_history_table(self):
        columns = ("Bus Company", "Origin", "Destination", "Time", "Bus Type", "Fare")
        table = ttk.Treeview(self.frame, columns=columns, show="headings", selectmode="browse")
        table.pack(fill="both", expand=True)

        self.fetch_and_display_history(table)
        self.add_table_headings(table, columns)

    def fetch_and_display_history(self, table):
        conn = sqlite3.connect('history.db')
        cur = conn.cursor()
        cur.execute("SELECT bus_company, origin, destination, time, bus_type, fare FROM history WHERE username=?",
                    (self.username,))
        tickets_data = cur.fetchall()
        conn.close()

        for row in tickets_data:
            table.insert("", "end", values=row)

    def add_table_headings(self, table, columns):
        for col in columns:
            table.heading(col, text=col)
            table.column(col, width=100)


class LogoutMenu:
    def __init__(self, root):
        self.root = root


def create_new_sidebar(username):
    root = tk.Tk()
    root.title("Bus Connect")
    root.resizable(False, False)
    root.geometry("1100x600")

    sidebar_frame = tk.Frame(root, bg="#F2F2EB", width=180)
    sidebar_frame.pack(side="left", fill="y")

    # Open and resize the image
    img = Image.open("bus.png")
    img = img.resize((78, 90))  # Adjust the size as needed

    # Convert the image for tkinter
    img_tk = ImageTk.PhotoImage(img)

    # Add a label to display the image
    image_label = ttk.Label(sidebar_frame, image=img_tk)
    image_label.image = img_tk  # Keep a reference to avoid garbage collection
    image_label.pack(side="top", fill="x", pady=(50, 50), padx=40)  # Added padx to center the image

    sidebar_contents = [("Bus Schedule", BusScheduleMenu, "Arial", 10, "#000000"),  # Font info added
                        ("Tickets", TicketsMenu, "Arial", 10, "#000000"),  # Font info added
                        ("Notifications", NotificationsMenu, "Arial", 10, "#000000"),  # Font info added
                        ("History", HistoryMenu, "Arial", 10, "#000000"),  # Font info added
                        ("Change Profile", ProfileMenu, "Arial", 10, "#000000"),  # Font info added
                        ("Log Out", LogoutMenu, "Arial", 10, "#FF0000")]  # Font info added

    main_content_frame = tk.Frame(root, bg="#401B1B")
    main_content_frame.pack(side="left", fill="both", expand=True)

    tickets_menu = TicketsMenu(main_content_frame, username=username)

    def display_menu(menu_class, username):
        if menu_class == LogoutMenu:
            root.destroy()
        else:
            for widget in main_content_frame.winfo_children():
                widget.destroy()
            menu = menu_class(main_content_frame, username=username)  # Pass username to relevant menus
            menu.display()

    for i, (item, menu_class, font_family, font_size, font_color) in enumerate(sidebar_contents):
        if i == 0:
            separator_top = ttk.Separator(sidebar_frame, orient="horizontal")
            separator_top.pack(fill="x", pady=(0, 5), padx=5)
        btn = tk.Button(sidebar_frame, text=item, width=20, bg="#F2F2EB", fg=font_color, bd=0,
                        font=(font_family, font_size),  # Set font properties
                        command=lambda x=menu_class: display_menu(x, username))
        btn.pack(side="top", pady=5)
        if item != "Log Out":
            separator = ttk.Separator(sidebar_frame, orient="horizontal")
            separator.pack(fill="x", pady=5, padx=5)
        if i == len(sidebar_contents) - 1:
            separator_bottom = ttk.Separator(sidebar_frame, orient="horizontal")
            separator_bottom.pack(fill="x", pady=(5, 0), padx=5)

    root.mainloop()


if __name__ == "__main__":
    create_new_sidebar("username")
