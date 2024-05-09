import sqlite3
import random
import string
from tkinter import messagebox
def initialize_database():
    with sqlite3.connect('tickets.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS tickets
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT,
                      ticket_id TEXT UNIQUE,
                      bus_company TEXT,  -- Add the missing column here
                      origin TEXT,
                      destination TEXT,
                      time TEXT,
                      bus_type TEXT,
                      fare REAL)''')

def create_ticket(length):
    characters = string.ascii_uppercase + string.digits
    ticket = ''.join(random.choice(characters) for i in range(length))
    return ticket

def is_ticket_unique(ticket):
    with sqlite3.connect('tickets.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT ticket_id FROM tickets WHERE ticket_id=?", (ticket,))
        existing_ticket = cur.fetchone()
        return existing_ticket is None

def create_ticket_id():
    ticket_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    with sqlite3.connect('tickets.db') as conn:
        c = conn.cursor()
        while True:
            c.execute("SELECT * FROM tickets WHERE ticket_id=?", (ticket_id,))
            if c.fetchone() is None:
                break
            ticket_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return ticket_id

def ticket_callback(username, bus_company, origin, destination, time, bus_type, fare):
    ticket_id = create_ticket_id()
    with sqlite3.connect('tickets.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO tickets (username, ticket_id, bus_company, origin, destination, time, bus_type, fare) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (username, ticket_id, bus_company, origin, destination, time, bus_type, fare))
        conn.commit()
    messagebox.showinfo("Ticket Generated", f"Ticket Generated: {ticket_id}")

# Initialize the database
initialize_database()
