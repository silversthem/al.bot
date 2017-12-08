import sqlite3

users_db = sqlite3.connect('sessions.sqlite')

users_db.execute('''
CREATE TABLE Session (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    answer text
)''')

users_db.commit()

users_db.execute('''
CREATE TABLE Session_Step (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id int,
    question text,
    answer text,
    parameter text,
    predicat_type text,
    value text,
    FOREIGN KEY(session_id) REFERENCES Session(id)
)''')

users_db.commit()

users_db.close()
