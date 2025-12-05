# Cities Database
# Dalila Spencer
# 2025-12-04

import sqlite3

# connect to database
conn = sqlite3.connect('cities.db')

# create cursor
cur = conn.cursor()


cur.execute('SELECT * FROM Cities')

results = cur.fetchall()

for row in results:
    print(f'{row[0]:<10}{row[1]:20}{row[2]:,.0f}')


