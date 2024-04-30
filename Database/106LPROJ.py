import sqlite3

#creation database
conn= sqlite3.connect('C:\\Users\\User\\Desktop\\106L\\106LPROJ.db')

#creation cursor
cur= conn.cursor()

#create table
cur.execute('''CREATE TABLE IF NOT EXISTS
            joybus_info(Bus Company Name TEXT, Origin TEXT, Destination TEXT, Time TEXT, Bus Type TEXT, Fare INT)
''')

joybus1_list = [
    ("JoyBus", "Cubao", "Baguio", "12:01 AM", "Deluxe", 720),
    ("JoyBus", "Cubao", "Baguio", "02:30 AM", "Premier", 740),
    ("JoyBus", "Cubao", "Baguio", "03:30 AM", "Deluxe", 720),
    ("JoyBus", "Cubao", "Baguio", "04:30 AM", "Premier", 740),
    ("JoyBus", "Cubao", "Baguio", "08:30 AM", "Deluxe", 720),
    ("JoyBus", "Cubao", "Baguio", "11:00 AM", "Deluxe", 720),
    ("JoyBus", "Cubao", "Baguio", "12:00 PM", "Premier", 740),
    ("JoyBus", "Cubao", "Baguio", "02:00 PM", "Deluxe", 720),
    ("JoyBus", "Cubao", "Baguio", "04:00 PM", "Premier", 740),
    ("JoyBus", "Cubao", "Baguio", "06:00 PM", "Deluxe", 720),
    ("JoyBus", "Cubao", "Baguio", "08:00 PM", "Deluxe", 720),
    ("JoyBus", "Cubao", "Baguio", "10:00 PM", "Deluxe", 720),
    ("JoyBus", "Cubao", "Baguio", "11:00 PM", "Deluxe", 720)
]

cur.executemany("INSERT INTO joybus_info VALUES (?,?,?,?,?,?)", joybus1_list)

joybus2_list = [
    ("JoyBus", "Pasay", "Baguio", "12:01 AM", "Deluxe", 730),
    ("JoyBus", "Pasay", "Baguio", "01:30 AM", "Premier", 760),
    ("JoyBus", "Pasay", "Baguio", "02:30 AM", "Deluxe", 730),
    ("JoyBus", "Pasay", "Baguio", "03:30 AM", "Premier", 760),
    ("JoyBus", "Pasay", "Baguio", "08:30 AM", "Deluxe", 730),
    ("JoyBus", "Pasay", "Baguio", "10:00 AM", "Deluxe", 730),
    ("JoyBus", "Pasay", "Baguio", "11:00 PM", "Premier", 760),
    ("JoyBus", "Pasay", "Baguio", "01:00 PM", "Deluxe", 730),
    ("JoyBus", "Pasay", "Baguio", "02:30 PM", "Deluxe", 730),
    ("JoyBus", "Pasay", "Baguio", "04:00 PM", "Premier", 760),
    ("JoyBus", "Pasay", "Baguio", "06:00 PM", "Deluxe", 730),
    ("JoyBus", "Pasay", "Baguio", "09:30 PM", "Deluxe", 730)
]

cur.executemany("INSERT INTO joybus_info VALUES (?,?,?,?,?,?)", joybus2_list)

joybus3_list = [
    ("JoyBus", "Baguio", "Pasay", "12:00 AM", "Premier", 760),
    ("JoyBus", "Baguio", "Pasay", "02:00 AM", "Deluxe", 730),
    ("JoyBus", "Baguio", "Pasay", "03:00 AM", "Deluxe", 730),
    ("JoyBus", "Baguio", "Pasay", "06:00 AM", "Premier", 760),
    ("JoyBus", "Baguio", "Pasay", "08:00 AM", "Deluxe", 720),
    ("JoyBus", "Baguio", "Pasay", "10:00 AM", "Premier", 740),
    ("JoyBus", "Baguio", "Pasay", "12:00 PM", "Deluxe", 730),
    ("JoyBus", "Baguio", "Pasay", "02:00 PM", "Premier", 740),
    ("JoyBus", "Baguio", "Pasay", "04:00 PM", "Deluxe", 730),
    ("JoyBus", "Baguio", "Pasay", "06:00 PM", "Premier", 760),
    ("JoyBus", "Baguio", "Pasay", "08:00 PM", "Deluxe", 730),
    ("JoyBus", "Baguio", "Pasay", "09:00 PM", "Premier", 760),
    ("JoyBus", "Baguio", "Pasay", "10:00 PM", "Deluxe", 730),
    ("JoyBus", "Baguio", "Pasay", "11:00 PM", "Deluxe", 730),
    ("JoyBus", "Baguio", "Trinoma", "01:00 AM", "Premier", 740),
    ("JoyBus", "Baguio", "Trinoma", "05:00 AM", "Premier", 740),
    ("JoyBus", "Baguio", "Trinoma", "07:00 AM", "Premier", 740),
    ("JoyBus", "Baguio", "Trinoma", "11:00 AM", "Deluxe", 720),
    ("JoyBus", "Baguio", "Trinoma", "07:00 PM", "Deluxe", 720),
    ("JoyBus", "Baguio", "Avenida", "01:45 AM", "Deluxe", 720),
    ("JoyBus", "Baguio", "Avenida", "10:30 AM", "Deluxe", 720),
    ("JoyBus", "Baguio", "Avenida", "02:00 PM", "Deluxe", 720),
    ("JoyBus", "Baguio", "Avenida", "09:30 PM", "Deluxe", 720),
    ("JoyBus", "Baguio", "Avenida", "10:30 PM", "Deluxe", 720)
]

cur.executemany("INSERT INTO joybus_info VALUES (?,?,?,?,?,?)", joybus3_list)

cur.execute('''CREATE TABLE IF NOT EXISTS
            fariñas_info(Bus Company Name TEXT, Origin TEXT, Destination TEXT, Time TEXT, Bus Type TEXT, Fare INT)
''')

fariñas_list = [
    ("Fariñas", "Laoag", "Manila", "07:00 AM", "First Class", 1000),
    ("Fariñas", "Laoag", "Manila", "12:30 PM", "First Class", 1000),
    ("Fariñas", "Laoag", "Manila", "06:00 PM", "First Class", 1000),
    ("Fariñas", "Laoag", "Manila", "07:00 PM", "First Class", 1000),
    ("Fariñas", "Laoag", "Manila", "08:00 PM", "First Class", 1000),
    ("Fariñas", "Laoag", "Manila", "08:30 PM", "First Class", 1000),
    ("Fariñas", "Laoag", "Manila", "09:00 PM", "First Class", 1000),
    ("Fariñas", "Laoag", "Manila", "09:30 PM", "First Class", 1000),
    ("Fariñas", "Laoag", "Manila", "10:00 PM", "Super Deluxe", 1100),
    ("Fariñas", "Laoag", "Manila", "10:30 PM", "Super First Class", 1000),
    ("Fariñas", "Laoag", "Manila", "11:00 PM", "Super Deluxe", 1000)
]

cur.executemany("INSERT INTO fariñas_info VALUES (?,?,?,?,?,?)", fariñas_list)

cur.execute('''CREATE TABLE IF NOT EXISTS
            partas_info(Bus Company Name TEXT, Origin TEXT, Destination TEXT, Time TEXT, Bus Type TEXT, Fare INT)
''')

partas1_list = [
    ("Partas", "Manila", "La Union", "9:00 AM", "Deluxe", 1000),
    ("Partas", "Manila", "La Union", "4:00 PM", "Deluxe", 1000),
    ("Partas", "Manila", "La Union", "7:00 PM", "Deluxe", 1000),
    ("Partas", "Manila", "La Union", "8:00 PM", "Deluxe", 1000),
    ("Partas", "Manila", "La Union", "8:00 PM", "Super Deluxe", 1200),
    ("Partas", "Manila", "La Union", "9:00 PM", "Super Deluxe", 1200),
    ("Partas", "Manila", "La Union", "10:00 PM", "Super Deluxe", 1200),
    ("Partas", "Manila", "La Union", "11:55 PM", "Deluxe", 1000)
]

cur.executemany("INSERT INTO partas_info VALUES (?,?,?,?,?,?)", partas1_list)

partas2_list = [
    ("Partas", "Manila", "Laoag", "2:00 PM", "Deluxe", 1200),
    ("Partas", "Manila", "Laoag", "7:00 PM", "Super Deluxe", 1500),
    ("Partas", "Manila", "Laoag", "9:00 PM", "Super Deluxe", 1500)
]

cur.executemany("INSERT INTO partas_info VALUES (?,?,?,?,?,?)", partas2_list)

partas3_list = [
    ("Partas", "Manila", "Vigan", "9:00 PM", "Deluxe", 1200),
    ("Partas", "Manila", "Vigan", "10:00 PM", "Deluxe", 1200),
    ("Partas", "Manila", "Vigan", "11:00 PM", "Deluxe", 1200)
]

cur.executemany("INSERT INTO partas_info VALUES (?,?,?,?,?,?)", partas3_list)

partas4_list = [
    ("Partas", "La Union", "Manila", "3:30 PM", "Super Deluxe", 1200),
    ("Partas", "La Union", "Manila", "9:00 PM", "Deluxe", 1000)
]

cur.executemany("INSERT INTO partas_info VALUES (?,?,?,?,?,?)", partas4_list)

partas5_list = [
    ("Partas", "Laoag", "Manila", "6:00 PM", "Super Deluxe", 1500),
    ("Partas", "Laoag", "Manila", "8:00 PM", "Super Deluxe", 1500),
    ("Partas", "Laoag", "Manila", "8:30 PM", "Deluxe", 1200)
]

cur.executemany("INSERT INTO partas_info VALUES (?,?,?,?,?,?)", partas5_list)

cur.execute('''CREATE TABLE IF NOT EXISTS
            user_info(Name TEXT, Username TEXT, Email TEXT, Password TEXT, Age INT, Address TEXT)
''')

user_list = [
    ("John Smith", "johnsmith87", "john.smith@example.com", "password123", 35, "123 Main St, Anytown, USA"),
    ("Emily Johnson", "emilyj", "emily.johnson@example.com", "emily123", 28, "456 Elm St, Springfield, USA"),
    ("Michael Brown", "mbrown", "michael.b@example.com", "pass456", 42, "789 Oak St, Metro City, USA"),
    ("Sarah Miller", "sarahm", "s.miller@example.com", "sarahpass", 25, "321 Pine St, Smalltown, USA")
]

cur.executemany("INSERT INTO user_info VALUES (?,?,?,?,?,?)", partas5_list)

conn.commit()

cur.close()

conn.close()