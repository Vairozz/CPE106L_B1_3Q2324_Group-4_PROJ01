import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from ticket_functions import create_ticket, is_ticket_unique, ticket_callback
from history_database import *
class ProfileMenu:
    def __init__(self, root):
        self.root = root

    def display(self):
        label = tk.Label(self.root, text="Profile Page", font=("Arial", 18))
        label.pack(fill="both", expand=True)

class BusScheduleMenu:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.selected_item = None

    def display(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

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

            generate_button = ttk.Button(tab_frame, text="Generate Ticket", command=lambda t=table: self.generate_ticket(t))
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
        columns = ("Ticket ID", "Bus Company", "Origin", "Destination", "Time", "Bus Type", "Fare")  # Include "Ticket ID"
        table = ttk.Treeview(self.frame, columns=columns, show="headings", selectmode="browse")
        table.pack(fill="both", expand=True)
        
        self.fetch_and_display_tickets(table)
        self.add_table_headings(table, columns)

    def fetch_and_display_tickets(self, table):
        conn = sqlite3.connect('tickets.db')
        cur = conn.cursor()
        cur.execute("SELECT ticket_id, bus_company, origin, destination, time, bus_type, fare FROM tickets WHERE username=?", (self.username,))
        tickets_data = cur.fetchall()
        conn.close()

        for row in tickets_data:
            table.insert("", "end", values=row)

    def add_table_headings(self, table, columns):
        for col in columns:
            table.heading(col, text=col)
            table.column(col, width=100)  # Adjust column width as needed

class NotificationsMenu:
    def __init__(self, root, username):  # Modify to accept username
        self.root = root

    def display(self):
        label = tk.Label(self.root, text="Notifications Page", font=("Arial", 18))
        label.pack(fill="both", expand=True)

class HistoryMenu:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

    def display(self):
        self.create_history_table()

    def create_history_table(self):
        columns = ( "Bus Company", "Origin", "Destination", "Time", "Bus Type", "Fare")
        table = ttk.Treeview(self.frame, columns=columns, show="headings", selectmode="browse")
        table.pack(fill="both", expand=True)

        self.fetch_and_display_history(table)
        self.add_table_headings(table, columns)

    def fetch_and_display_history(self, table):
        conn = sqlite3.connect('history.db')
        cur = conn.cursor()
        cur.execute("SELECT bus_company, origin, destination, time, bus_type, fare FROM history WHERE username=?", (self.username,))
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

    sidebar_frame = tk.Frame(root, bg="black", width=180)
    sidebar_frame.pack(side="left", fill="y")

    title_label = tk.Label(sidebar_frame, text="   BusConnect   ", font=("Arial", 18, "bold"), bg="black", fg="white")
    title_label.pack(side="top", fill="x", pady=(50, 50))

    sidebar_contents = [("Profile", ProfileMenu), ("Bus Schedule", BusScheduleMenu), ("Tickets", TicketsMenu),
                        ("Notifications", NotificationsMenu), ("History", HistoryMenu), ("Log Out", LogoutMenu)]

    main_content_frame = tk.Frame(root, bg="white")
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

    for i, (item, menu_class) in enumerate(sidebar_contents):
        if i == 0:
            separator_top = ttk.Separator(sidebar_frame, orient="horizontal")
            separator_top.pack(fill="x", pady=(0, 5), padx=5)
        btn = tk.Button(sidebar_frame, text=item, width=20, bg="black", fg="white", bd=0,
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
