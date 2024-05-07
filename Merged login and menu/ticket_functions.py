import sqlite3
import random
import string

def initialize_database():
    with sqlite3.connect('tickets.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS tickets
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT,
                      ticket_id TEXT UNIQUE,
                      ticket_data TEXT)''')
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

def ticket_callback(username, ticket_data):
    ticket_id = create_ticket_id()
    with sqlite3.connect('tickets.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO tickets (username, ticket_id, ticket_data) VALUES (?, ?, ?)", (username, ticket_id, ticket_data))
        conn.commit()
    print("Generated Ticket ID:", ticket_id)

initialize_database()
