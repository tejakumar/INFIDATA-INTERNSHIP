import tkinter as tk
import sqlite3

# Creating a connection object
conn = sqlite3.connect('registration.db')

# Creating a cursor object
cursor = conn.cursor()

# Creating a table to store registration details
cursor.execute('''CREATE TABLE IF NOT EXISTS registration (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL)''')

# Function to insert data into the table
def insert_data(name, email, phone):
    cursor.execute('''INSERT INTO registration (name, email, phone)
                      VALUES (?, ?, ?)''', (name, email, phone))
    conn.commit()

# Function to update data in the table
def update_data(id, name, email, phone):
    cursor.execute('''UPDATE registration SET name = ?, email = ?, phone = ?
                      WHERE id = ?''', (name, email, phone, id))
    conn.commit()

# Function to delete data from the table
def delete_data(id):
    cursor.execute('''DELETE FROM registration WHERE id = ?''', (id,))
    conn.commit()

# Function to display all records from the table
def display_data():
    cursor.execute('''SELECT * FROM registration''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Creating a GUI window
window = tk.Tk()
window.title('Registration Form')

# Creating labels and entry widgets for name, email and phone number
name_label = tk.Label(window, text='Name')
name_label.grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

email_label = tk.Label(window, text='Email')
email_label.grid(row=1, column=0)
email_entry = tk.Entry(window)
email_entry.grid(row=1, column=1)

phone_label = tk.Label(window, text='Phone')
phone_label.grid(row=2, column=0)
phone_entry = tk.Entry(window)
phone_entry.grid(row=2, column=1)

# Creating buttons for inserting/updating/deleting/displaying records
insert_button = tk.Button(window, text='Insert', command=lambda: insert_data(name_entry.get(), email_entry.get(), phone_entry.get()))
insert_button.grid(row=3, column=0)

update_button = tk.Button(window, text='Update', command=lambda: update_data(id_entry.get(), name_entry.get(), email_entry.get(), phone_entry.get()))
update_button.grid(row=3, column=1)

delete_button = tk.Button(window, text='Delete', command=lambda: delete_data(id_entry.get()))
delete_button.grid(row=4, column=0)

display_button = tk.Button(window, text='Display', command=lambda: display_data())
display_button.grid(row=4, column=1)

id_label = tk.Label(window, text='ID')
id_label.grid(row=5, column=0)
id_entry = tk.Entry(window)
id_entry.grid(row=5, column=1)

window.mainloop()