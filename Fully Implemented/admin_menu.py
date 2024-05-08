import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk
from ticket_functions import create_ticket, is_ticket_unique, ticket_callback
from history_database import history_callback




class AdminScheduleMenu:
    def __init__(self, root):
        self.root = root
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        # Create a Notebook (tabs container)
        self.notebook = ttk.Notebook(self.frame)
        self.notebook.pack(fill="both", expand=True)

        # Add tabs for each table
        self.add_schedule_tab("JoyBus Schedule", "joybus_info")
        self.add_schedule_tab("Fariñas Schedule", "fariñas_info")
        self.add_schedule_tab("Partas Schedule", "partas_info")

    def add_schedule_tab(self, tab_title, table_name):
        # Create a new tab
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text=tab_title)

        # Create table within the tab
        columns = ("Bus Company", "Origin", "Destination", "Time", "Bus Type", "Fare")
        table = ttk.Treeview(tab, columns=columns, show="headings", selectmode="browse")
        table.pack(fill="both", expand=True)

        # Fetch and display data in the table
        self.fetch_and_display_schedule(table, table_name)
        self.add_table_headings(table, columns)
        self.add_delete_buttons(table, table_name)

        # Add Schedule Button
        add_button = ttk.Button(tab, text="Add Schedule", command=lambda: self.add_schedule_popup(table, table_name))
        add_button.pack(pady=10)

    def fetch_and_display_schedule(self, table, table_name):
        conn = sqlite3.connect('106LPROJ.db')
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table_name} ORDER BY rowid DESC")
        schedule_data = cur.fetchall()
        conn.close()

        for row in schedule_data:
            table.insert("", "end", values=row)

    def add_table_headings(self, table, columns):
        for col in columns:
            table.heading(col, text=col)
            table.column(col, width=100)    

    def add_delete_buttons(self, table, table_name):
        def delete_schedule():
            selected_item = table.selection()
            if selected_item:
            # Get all relevant values from the selected item
                bus_info = table.item(selected_item, "values")
                bus = bus_info[0]
                origin = bus_info[1]
                destination = bus_info[2]
                time = bus_info[3]
                bus_type = bus_info[4]
                fare = bus_info[5]

                conn = sqlite3.connect('106LPROJ.db')
                cur = conn.cursor()
                cur.execute(f"DELETE FROM {table_name} WHERE Bus=? AND Origin=? AND Destination=? AND Time=? AND Type=? AND Fare=?",
                        (bus, origin, destination, time, bus_type, fare))
                conn.commit()
                conn.close()

                table.delete(selected_item)

        delete_button = ttk.Button(table.master, text="Delete Schedule", command=delete_schedule)
        delete_button.pack(pady=10)

    def add_schedule_popup(self, table, table_name):
        popup = tk.Toplevel()
        popup.title("Add Schedule")

        # Pre-specified bus companies
        bus_companies = ["JoyBus", "Fariñas", "Partas"]

        # Dropdown for bus company selection
        bus_company_label = ttk.Label(popup, text="Bus Company:")
        bus_company_label.pack(padx=10, pady=5)
        bus_company_var = tk.StringVar()
        bus_company_dropdown = ttk.Combobox(popup, textvariable=bus_company_var, values=bus_companies)
        bus_company_dropdown.pack(padx=10, pady=5)
        bus_company_dropdown.current(0)

        # Entry fields for other details
        origin_label = ttk.Label(popup, text="Origin:")
        origin_label.pack(padx=10, pady=5)
        origin_entry = ttk.Entry(popup)
        origin_entry.pack(padx=10, pady=5)

        destination_label = ttk.Label(popup, text="Destination:")
        destination_label.pack(padx=10, pady=5)
        destination_entry = ttk.Entry(popup)
        destination_entry.pack(padx=10, pady=5)

        time_label = ttk.Label(popup, text="Time:")
        time_label.pack(padx=10, pady=5)
        time_entry = ttk.Entry(popup)
        time_entry.pack(padx=10, pady=5)

        bus_type_label = ttk.Label(popup, text="Bus Type:")
        bus_type_label.pack(padx=10, pady=5)
        bus_type_entry = ttk.Entry(popup)
        bus_type_entry.pack(padx=10, pady=5)

        fare_label = ttk.Label(popup, text="Fare:")
        fare_label.pack(padx=10, pady=5)
        fare_entry = ttk.Entry(popup)
        fare_entry.pack(padx=10, pady=5)

        # Save button
        def save_schedule():
            bus_company = bus_company_var.get()
            origin = origin_entry.get()
            destination = destination_entry.get()
            time = time_entry.get()
            bus_type = bus_type_entry.get()
            fare = fare_entry.get()

            if bus_company and origin and destination and time and bus_type and fare:
                # Check if fare is a valid number
                try:
                    float(fare)
                except ValueError:
                    ttk.Label(popup, text="Fare must be a number!", foreground="red").pack(padx=10, pady=5)
                    return

                conn = sqlite3.connect('106LPROJ.db')
                cur = conn.cursor()
                cur.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?, ?)",
                            (bus_company, origin, destination, time, bus_type, fare))
                conn.commit()
                conn.close()
                popup.destroy()
                # Refresh the table after adding the schedule
                self.refresh_table(table_name)
            else:
                ttk.Label(popup, text="Please fill in all fields!", foreground="red").pack(padx=10, pady=5)

        save_button = ttk.Button(popup, text="Save", command=save_schedule)
        save_button.pack(padx=10, pady=10)

    def refresh_table(self, table_name):
        for tab in self.notebook.tabs():
            if self.notebook.tab(tab, "text") == "JoyBus Schedule" and table_name == "joybus_info":
                self.notebook.tab(tab, state="hidden")
                self.notebook.tab(tab, state="normal")
            elif self.notebook.tab(tab, "text") == "Fariñas Schedule" and table_name == "fariñas_info":
                self.notebook.tab(tab, state="hidden")
                self.notebook.tab(tab, state="normal")
            elif self.notebook.tab(tab, "text") == "Partas Schedule" and table_name == "partas_info":
                self.notebook.tab(tab, state="hidden")
                self.notebook.tab(tab, state="normal")







class TicketsMenu:
    def __init__(self, root):
        self.root = root
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

    def display(self):
        self.create_ticket_table()

    def create_ticket_table(self):
        columns = ("Ticket ID", "Bus Company", "Origin", "Destination", "Time", "Bus Type", "Fare", "Actions")
        self.table = ttk.Treeview(self.frame, columns=columns, show="headings", selectmode="browse")
        self.table.pack(fill="both", expand=True)

        self.fetch_and_display_tickets(self.table)
        self.add_table_headings(self.table, columns)
        self.add_delete_buttons(self.table)
        self.add_search_entry()

    def fetch_and_display_tickets(self, table):
        conn = sqlite3.connect('tickets.db')
        cur = conn.cursor()
        cur.execute("SELECT ticket_id, bus_company, origin, destination, time, bus_type, fare FROM tickets")
        tickets_data = cur.fetchall()
        conn.close()

        for row in tickets_data:
            table.insert("", "end", values=row)

    def add_table_headings(self, table, columns):
        for col in columns:
            table.heading(col, text=col)
            table.column(col, width=100)

    def add_delete_buttons(self, table):
        def delete_ticket():
            selected_item = table.selection()
            if selected_item:
                ticket_id = table.item(selected_item, "values")[0]  # Get the ticket ID
                # Delete the ticket from the database
                conn = sqlite3.connect('tickets.db')
                cur = conn.cursor()
                cur.execute("DELETE FROM tickets WHERE ticket_id=?", (ticket_id,))
                conn.commit()
                conn.close()
                # Remove the ticket from the table
                table.delete(selected_item)

        delete_button = ttk.Button(self.frame, text="Delete Ticket", command=delete_ticket)
        delete_button.pack(pady=10)

    def add_search_entry(self):
        search_label_text = "Search Ticket ID Here:"
        search_label = tk.Label(self.frame, text=search_label_text, font=("Arial", 10))
        search_label.pack()

        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(self.frame, textvariable=self.search_var)
        self.search_entry.pack(pady=(0, 10))  # Adjust the pady values to position the entry box below the label
        self.search_var.trace_add("write", self.update_search)


    def update_search(self, *args):
        search_text = self.search_var.get().strip()
        if search_text:
            for item in self.table.get_children():
                if self.table.item(item, "values")[0].startswith(search_text):
                    self.table.selection_set(item)
                    self.table.focus(item)
                    break
            else:
                messagebox.showinfo("Ticket Not Found", f"Ticket with ID starting with {search_text} not found.")
        else:
            self.table.selection_remove(self.table.selection())
            self.table.focus("")




 # Adjust column width as needed

class AdminNotificationsMenu:
    def __init__(self, root):
        self.root = root
        self.company_name_var = tk.StringVar()
        self.notification_text = tk.StringVar()

    def display(self):
        company_label = tk.Label(self.root, text="Enter Bus Company Name:")
        company_label.pack()
        company_combobox = ttk.Combobox(self.root, textvariable=self.company_name_var, values=["JOYBUS", "FARIÑAS", "PARTAS"])
        company_combobox.pack()

        notification_label = tk.Label(self.root, text="Enter Notification:")
        notification_label.pack()
        notification_entry = tk.Text(self.root, height=5, width=30, wrap=tk.WORD, font=("Arial", 10), padx=5, pady=5)
        notification_entry.pack()

        notify_button = ttk.Button(self.root, text="Notify Users", command=self.notify_users)
        notify_button.pack()

        def check_completeness(*args):
            if self.company_name_var.get().strip() and self.notification_text.get().strip():
                notify_button.config(state=tk.NORMAL)
            else:
                notify_button.config(state=tk.DISABLED)

        self.company_name_var.trace_add("write", check_completeness)
        self.notification_text.trace_add("write", check_completeness)

        notification_entry.bind("<KeyRelease>", lambda event: self.update_notification(notification_entry))

    def update_notification(self, notification_entry):
        self.notification_text.set(notification_entry.get("1.0", tk.END))

    def notify_users(self):
        company_name = self.company_name_var.get()
        notification = self.notification_text.get()

        conn = sqlite3.connect('notification.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS notifications (company_name TEXT, notification TEXT)")
        cur.execute("INSERT INTO notifications VALUES (?, ?)", (company_name, notification))
        conn.commit()
        conn.close()
        messagebox.showinfo("Notification Sent", "Notification sent to users.")





class HistoryMenu:
    def __init__(self, root):
        self.root = root
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

    def display(self):
        self.create_history_table()

    def create_history_table(self):
        columns = ("Username","Bus Company", "Origin", "Destination", "Time", "Bus Type", "Fare")
        table = ttk.Treeview(self.frame, columns=columns, show="headings", selectmode="browse")
        table.pack(fill="both", expand=True)

        self.fetch_and_display_history(table)
        self.add_table_headings(table, columns)

    def fetch_and_display_history(self, table):
        conn = sqlite3.connect('history.db')
        cur = conn.cursor()
        cur.execute("SELECT username, bus_company, origin, destination, time, bus_type, fare FROM history")
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


def create_admin_menu():
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

    sidebar_contents = [("Edit Bus Schedule", AdminScheduleMenu, "Arial", 10, "#000000"),  # Font info added
                        ("Claim Tickets", TicketsMenu, "Arial", 10, "#000000"),  # Font info added
                        ("Create Notifications", AdminNotificationsMenu, "Arial", 10, "#000000"),  # Font info added
                        ("See History", HistoryMenu, "Arial", 10, "#000000"),  # Font info added,  # Font info added
                        ("Log Out", LogoutMenu, "Arial", 10, "#FF0000")]  # Font info added

    main_content_frame = tk.Frame(root, bg="#401B1B")
    main_content_frame.pack(side="left", fill="both", expand=True)

    tickets_menu = TicketsMenu(main_content_frame)

    def display_menu(menu_class):
        if menu_class == LogoutMenu:
            root.destroy()
        else:
            for widget in main_content_frame.winfo_children():
                widget.destroy()
            menu = menu_class(main_content_frame)  # Pass username to relevant menus
            menu.display()

    for i, (item, menu_class, font_family, font_size, font_color) in enumerate(sidebar_contents):
        if i == 0:
            separator_top = ttk.Separator(sidebar_frame, orient="horizontal")
            separator_top.pack(fill="x", pady=(0, 5), padx=5)
        btn = tk.Button(sidebar_frame, text=item, width=20, bg="#F2F2EB", fg=font_color, bd=0,
                        font=(font_family, font_size),  # Set font properties
                        command=lambda x=menu_class: display_menu(x))
        btn.pack(side="top", pady=5)
        if item != "Log Out":
            separator = ttk.Separator(sidebar_frame, orient="horizontal")
            separator.pack(fill="x", pady=5, padx=5)
        if i == len(sidebar_contents) - 1:
            separator_bottom = ttk.Separator(sidebar_frame, orient="horizontal")
            separator_bottom.pack(fill="x", pady=(5, 0), padx=5)

    root.mainloop()


if __name__ == "__main__":
    create_admin_menu()
