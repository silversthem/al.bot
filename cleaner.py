import sqlite3

db = sqlite3.connect('db/phones.sqlite')

cursor = db.cursor()

rows = cursor.execute('SELECT COUNT(*) FROM Phone JOIN Phys ON Phys.phone = Phone.id JOIN Camera ON Camera.phone = Phone.id JOIN Hardware ON Hardware.phone = Phone.id')

for row in rows:
    print(row)

db.close()
