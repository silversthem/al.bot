import sqlite3

phones_db = sqlite3.connect('phones.sqlite')

phones_db.execute('''
CREATE TABLE Phone (
    id int PRIMARY KEY,
    name text,
    constructor text,
    os text,
    price int
)''')

phones_db.commit()

phones_db.execute('''
CREATE TABLE Phys (
    phone int,
    size int,
    weight int,
    colors text,
    is_tactil short,
    moveable_battery short,
    FOREIGN KEY(phone) REFERENCES Phone(id)
)''')

phones_db.execute('''
CREATE TABLE Camera (
    phone int,
    back_res int,
    front_res int,
    flash short,
    autofocus short,
    score int,
    FOREIGN KEY(phone) REFERENCES Phone(id)
)
''')

phones_db.execute('''
CREATE TABLE Hardware (
    phone int,
    type_sim text,
    bluetooth text,
    cell_reception short,
    gps short,
    memory int,
    memory_upgrade short,
    ram int,
    processor text,
    battery_amp int,
    FOREIGN KEY(phone) REFERENCES Phone(id)
)
''')

phones_db.commit()

phones_db.close()
