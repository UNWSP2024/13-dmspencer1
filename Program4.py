# Phonebook Database pt2
# Dalila Spencer
# 2025-12-04

import sqlite3

def main():

    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    open_menu(cur)

    conn.close()

def open_menu(cur):
    print('\n****************************')
    print('1. Add a new phonebook entry')
    print('2. Delete a phonebook entry')
    print('3. Edit a phonebook entry')
    print('4. Search for a phonebook entry')
    print('5. Display all phonebook entries')
    print('6. Exit')
    print('****************************\n')
    choice = input('Enter the number for what you would like to do: ')

    if choice == '1':
        add_new_entry()
        open_menu(cur)
    if choice == '2':
        delete_entry()
        open_menu(cur)
    if choice == '3':
        edit_entry()
        open_menu(cur)
    if choice == '4':
        search_entry()
        open_menu(cur)
    if choice == '5':
        display_entries()
        input('Press Enter to continue...')
        open_menu(cur)
    else:
        return

def display_entries():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM Entries')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<5}{row[1]:30}{row[2]:20}')

def add_new_entry():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    new_name = input('Enter a name: ')
    new_number = input('Enter a phone number: ')
    cur.execute('''INSERT INTO Entries (Name, PhoneNumber)
    VALUES (?, ?)''', (new_name, new_number))

    print('New entry added.')
    input('Press Enter to continue...')

    conn.commit()

def delete_entry():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    display_entries()
    entry_number = input('Enter the ID of the entry you would like to delete: ')
    cur.execute('''DELETE FROM Entries WHERE EntryID = ?''', (entry_number,))

    print('Entry deleted.')
    input('Press Enter to continue...')

    conn.commit()

def edit_entry():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    display_entries()
    option = int(input('What is the ID of entry would you like to edit?: '))
    new_name = input('Enter a new name: ')
    new_number = input('Enter a new phone number: ')

    cur.execute('''UPDATE Entries
     SET Name = ?, PhoneNumber = ?
     WHERE EntryID = ?''', (new_name, new_number, option))

    print('Entry updated. ')
    input('Press Enter to continue...')

    conn.commit()

def search_entry():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    results = []

    search = input('Enter a name you would like to search for: ')
    results = cur.execute('''SELECT * FROM Entries WHERE Name = ?''', (search,))

    for row in results:
        print(f'{row[0]:<5}{row[1]:30}{row[2]:20}')

    input('Press Enter to continue...')



if __name__ == '__main__':
    main()
