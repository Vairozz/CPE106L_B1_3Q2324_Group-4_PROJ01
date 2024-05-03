import tkinter as tk
from tkinter import ttk

class AppWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.sidebar = Sidebar(self)
        self.sidebar.pack(side="left", fill="y")
        self.main_content = MainContent(self)
        self.main_content.pack(side="right", fill="both", expand=True)
        self.title("Bus Connect")
        self.resizable(False, False)
        self.geometry("1100x600") 

class Sidebar(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="black", width=200)
        self.create_widgets()

    def create_widgets(self):
        self.blankSpace()
        self.user_data = UserData(self, "Bus Connect")
        self.blankSpace()
        self.lineSeparator()
        self.displayButtons()

    def blankSpace(self):
        blankSpace = tk.Label(self, text=" ", bg="black", fg="white", height=3)
        blankSpace.pack(fill="x", padx=10)

    def displayButtons(self):
        button_texts = ["Profile", 
                        "Bus Companies", 
                        "Bus Schedule", 
                        "Tickets", 
                        "Notifications", 
                        "History", 
                        "Log Out"]
        for text in button_texts:
            command = self.displayTabs if text == "Bus Schedule" else (self.logout if text == "Log Out" else None)
            button = HoverButton(self, text, command)
            button.config(bg="black", fg="white", activebackground="white", activeforeground="black")
            button.pack(fill="x", padx=10, pady=5)
            self.lineSeparator()

    def lineSeparator(self):
        separator = tk.Frame(self, height=1, bg="gray")
        separator.pack(fill="x", padx=5, pady=(0, 5))

    def displayTabs(self):
        self.master.main_content.clearTabs()
        self.master.main_content.displayTabs()

    def logout(self):
        self.master.destroy()

class UserData:
    def __init__(self, master, name):
        container = tk.Frame(master, bg="black")
        container.pack(fill="x", padx=10, pady=(10, 0))
        info_frame = tk.Frame(container, bg="black")
        info_frame.pack(side="left", padx=(5, 0))
        name_label = tk.Label(info_frame, text=name + " ", font=("Arial", 20, "bold"), fg="white", bg="black")
        name_label.pack(anchor="w")

class HoverButton(tk.Button):
    def __init__(self, master=None, text=None, command=None):
        tk.Button.__init__(self, master, text=text, command=command, borderwidth=0, highlightthickness=0)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<ButtonRelease-1>", self.on_release)
        
    def on_enter(self, event):
        self.configure(bg="white", fg="black")
        
    def on_leave(self, event):
        self.configure(bg="black", fg="white")
        
    def on_press(self, event):
        self.configure(relief=tk.SUNKEN)
        
    def on_release(self, event):
        self.configure(relief=tk.RAISED)

class MainContent(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)
        self.tables = {}

    def clearTabs(self):
        for tab in self.notebook.winfo_children():
            self.notebook.forget(tab)

    def displayTabs(self):
        tabs = [("JOYBUS", "blue"), ("FARINAS", "green"), ("PARTAS", "red")]
        for title, color in tabs:
            tab = tk.Frame(self.notebook, bg="white")
            label = tk.Label(tab, text=title, font=("Arial", 24), fg=color, bg="white")
            label.pack(padx=20, pady=20)
            
            tree = ttk.Treeview(tab, columns=("1", "2", "3", "4", "5"), show="headings", height=10)
            tree.heading("#1", text="Origin")
            tree.heading("#2", text="Destination")
            tree.heading("#3", text="Departure Time")
            tree.heading("#4", text="Bus Type")
            tree.heading("#5", text="Fare (₱)")
            
            tree.column("#1", width=150)
            tree.column("#2", width=150)
            tree.column("#3", width=150)
            tree.column("#4", width=150)
            tree.column("#5", width=150)
            
            tree.pack(fill="both", expand=True)
            
            self.tables[title] = tree
            self.notebook.add(tab, text=title)

            #JOYBUS SCHEDULE
            if title == "JOYBUS":
                joybus_data = [
                    ("Cubao", "Baguio", "12:01 AM", "Deluxe", 720),
                    ("Cubao", "Baguio", "02:30 AM", "Premier", 740),
                    ("Cubao", "Baguio", "03:30 AM", "Deluxe", 720),
                    ("Cubao", "Baguio", "04:30 AM", "Premier", 740),
                    ("Cubao", "Baguio", "08:30 AM", "Deluxe", 720),
                    ("Cubao", "Baguio", "11:00 AM", "Deluxe", 720),
                    ("Cubao", "Baguio", "12:00 PM", "Premier", 740),
                    ("Cubao", "Baguio", "02:00 PM", "Deluxe", 720),
                    ("Cubao", "Baguio", "04:00 PM", "Premier", 740),
                    ("Cubao", "Baguio", "06:00 PM", "Deluxe", 720),
                    ("Cubao", "Baguio", "08:00 PM", "Deluxe", 720),
                    ("Cubao", "Baguio", "10:00 PM", "Deluxe", 720),
                    ("Cubao", "Baguio", "11:00 PM", "Deluxe", 720)
                ]
                for data in joybus_data:
                    tree.insert("", "end", values=data)
            
            #FARINAS SCHEDULE
            elif title == "FARINAS":
                farinas_data = [
                    ("Laoag", "Manila", "07:00 AM", "First Class", 1000),
                    ("Laoag", "Manila", "12:30 PM", "First Class", 1000),
                    ("Laoag", "Manila", "06:00 PM", "First Class", 1000),
                    ("Laoag", "Manila", "07:00 PM", "First Class", 1000),
                    ("Laoag", "Manila", "08:00 PM", "First Class", 1000),
                    ("Laoag", "Manila", "08:30 PM", "First Class", 1000),
                    ("Laoag", "Manila", "09:00 PM", "First Class", 1000),
                    ("Laoag", "Manila", "09:30 PM", "First Class", 1000),
                    ("Laoag", "Manila", "10:00 PM", "Super Deluxe", 1100),
                    ("Laoag", "Manila", "10:30 PM", "Super First Class", 1000),
                    ("Laoag", "Manila", "11:00 PM", "Super Deluxe", 1000)
                ]
                for data in farinas_data:
                    tree.insert("", "end", values=data)

            #PARTAS SCHEDULE
            elif title == "PARTAS":
                partas_data = [
                    ("Manila", "La Union", "9:00 AM", "Deluxe", 1000),
                    ("Manila", "La Union", "4:00 PM", "Deluxe", 1000),
                    ("Manila", "La Union", "7:00 PM", "Deluxe", 1000),
                    ("Manila", "La Union", "8:00 PM", "Deluxe", 1000),
                    ("Manila", "La Union", "8:00 PM", "Super Deluxe", 1200),
                    ("Manila", "La Union", "9:00 PM", "Super Deluxe", 1200),
                    ("Manila", "La Union", "10:00 PM", "Super Deluxe", 1200),
                    ("Manila", "La Union", "11:55 PM", "Deluxe", 1000)
                ]
                for data in partas_data:
                    tree.insert("", "end", values=data)

            self.tables[title] = tree
            self.notebook.add(tab, text=title)

if __name__ == "__main__":
    app = AppWindow()
    app.mainloop()
