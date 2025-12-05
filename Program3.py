# Phonebook Database
# Dalila Spencer
# 2025-12-04

import sqlite3

def main():

    # create connection
    conn = sqlite3.connect('phonebook.db')

    # create cursor
    cur = conn.cursor()

    # add entries table
    add_entries_table(cur)

    # add rows to the entries table
    add_entries(cur)

    # commit changes
    conn.commit()

    # display the entries
    display_entries(cur)

    # close the connection
    conn.close()


def add_entries_table(cur):
    cur.execute('DROP TABLE IF EXISTS Entries')
    # create table
    cur.execute('''CREATE TABLE Entries (EntryID INTEGER PRIMARY KEY NOT NULL,
                                            Name TEXT NOT NULL,
                                            PhoneNumber TEXT NOT NULL,)''')

def add_entries(cur):

    entries = [(1, 'Captain Jack Sparrow', '893-847-2184'),
               (2, 'Mickey Mouse', '123-456-7890'),
               (3, 'Loki Laufeyson', '443-868-3478'),
               (4, 'Inigo Montoya', '589-283-5849'),
               (5, 'Popeye the Sailor', '839-684-2944'),
               (6, 'Luke Skywalker', '349-539-2737'),
               (7, 'Count Dracula', '804-175-1398'),
               (8, 'Mary Poppins', '432-645-2923'),
               (9, 'Jeff', '238-694-5693'),
               (10, 'Albus Dumbledore', '299-454-8002')]

    for row in entries:
        cur.execute('''INSERT INTO Entries (EntryID, Name, PhoneNumber)
                       VALUES (?, ?, ?)''', (row[0], row[1], row[2]))


def display_entries(cur):
    print('Contents of entries.db/Entries table:')
    cur.execute('SELECT * FROM Entries')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<5}{row[1]:30}{row[2]:20}')


if __name__ == '__main__':
    main()