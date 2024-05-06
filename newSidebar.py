import tkinter as tk
from tkinter import ttk

class ProfileMenu:
    def __init__(self, root):
        self.root = root

    def display(self):
        label = tk.Label(self.root, text="Profile Page", font=("Arial", 18))
        label.pack(fill="both", expand=True)

class BusScheduleMenu:
    def __init__(self, root):
        self.root = root

    def display(self):
        notebook = ttk.Notebook(self.root)
        style = ttk.Style()
        style.configure("TNotebook", padding=5)
        style.configure("TNotebook.Tab", padding=[10, 5], font=('Arial', 10), tabposition='n', width=150, height=50)

        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        def read_schedule_data(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()[1:] 
                data = [line.strip().split(',') for line in lines]
                schedule = []
                for row in data:
                    schedule.append({
                        "Origin": row[0],
                        "Destination": row[1],
                        "Departure Time": row[2],
                        "Bus Type": row[3],
                        "Fare (₱)": row[4]
                    })
                return schedule

        tabs = [("JOYBUS Schedule", "joybusSched.txt"), 
                ("FARIÑAS Schedule", "farinasSched.txt"), 
                ("PARTAS Schedule", "partasSched.txt")
            ]
        for tab_name, file_name in tabs:
            tab_frame = ttk.Frame(notebook)
            notebook.add(tab_frame, text=tab_name)

            columns = ("Origin", "Destination", "Departure Time", "Bus Type", "Fare (₱)")
            table = ttk.Treeview(tab_frame, columns=columns, show="headings")
            table.pack(fill="both", expand=True)

            for col in columns:
                table.heading(col, text=col)
                table.column(col, width=100)

            schedule_data = read_schedule_data(file_name)
            for row in schedule_data:
                table.insert("", "end", 
                             values=(row["Origin"], row["Destination"], 
                                     row["Departure Time"], row["Bus Type"], 
                                     row["Fare (₱)"]))

class TicketsMenu:
    def __init__(self, root):
        self.root = root

    def display(self):
        label = tk.Label(self.root, text="Tickets Page", font=("Arial", 18))
        label.pack(fill="both", expand=True)

class NotificationsMenu:
    def __init__(self, root):
        self.root = root

    def display(self):
        label = tk.Label(self.root, text="Notifications Page", font=("Arial", 18))
        label.pack(fill="both", expand=True)

class HistoryMenu:
    def __init__(self, root):
        self.root = root

    def display(self):
        label = tk.Label(self.root, text="History Page", font=("Arial", 18))
        label.pack(fill="both", expand=True)

class LogoutMenu:
    def __init__(self, root):
        self.root = root

root = tk.Tk()
root.title("Bus Connect")
root.resizable(False, False)
root.geometry("1100x600") 

#SIDEBAR GRID FRAME
sidebar_frame = tk.Frame(root, bg="black", width=180)
sidebar_frame.pack(side="left", fill="y")

#SIDEBAR TITLE AND LAYOUT
title_label = tk.Label(sidebar_frame, text="   BusConnect   ", font=("Arial", 18, "bold"), bg="black", fg="white")
title_label.pack(side="top", fill="x", pady=(50, 50))

#SIDEBAR CONTENTS
sidebar_contents = [("Profile", ProfileMenu), ("Bus Schedule", BusScheduleMenu), ("Tickets", TicketsMenu),
                    ("Notifications", NotificationsMenu), ("History", HistoryMenu), ("Log Out", LogoutMenu)]

#DISPLAY THE SIDEBAR MENU
def display_menu(menu_class):
    if menu_class == LogoutMenu:
        root.destroy()
    else:
        for widget in main_content_frame.winfo_children():
            widget.destroy()
        menu = menu_class(main_content_frame)
        menu.display()

main_content_frame = tk.Frame(root, bg="white")
main_content_frame.pack(side="left", fill="both", expand=True)

#SIDEBAR BUTTONS AND LAYOUT
for i, (item, menu_class) in enumerate(sidebar_contents):
    if i == 0:
        separator_top = ttk.Separator(sidebar_frame, orient="horizontal")
        separator_top.pack(fill="x", pady=(0, 5), padx=5)
    btn = tk.Button(sidebar_frame, text=item, width=20, bg="black", fg="white", bd=0,
                    command=lambda x=menu_class: display_menu(x))
    btn.pack(side="top", pady=5)
    if item != "Log Out":
        separator = ttk.Separator(sidebar_frame, orient="horizontal")
        separator.pack(fill="x", pady=5, padx=5)
    if i == len(sidebar_contents) - 1:
        separator_bottom = ttk.Separator(sidebar_frame, orient="horizontal")
        separator_bottom.pack(fill="x", pady=(5, 0), padx=5)

root.mainloop()