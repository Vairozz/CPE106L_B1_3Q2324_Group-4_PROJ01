import sqlite3
import random
import string
from tkinter import messagebox
def initialize_database():
    with sqlite3.connect('history.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS history
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT,
                      ticket_id TEXT UNIQUE,
                      bus_company TEXT,  -- Add the missing column here
                      origin TEXT,
                      destination TEXT,
                      time TEXT,
                      bus_type TEXT,
                      fare REAL)''')




def history_callback(username, bus_company, origin, destination, time, bus_type, fare):
    with sqlite3.connect('history.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO history (username, bus_company, origin, destination, time, bus_type, fare) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (username, bus_company, origin, destination, time, bus_type, fare))
        conn.commit()


# Initialize the database
initialize_database()
