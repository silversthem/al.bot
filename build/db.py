import sqlite3

phones_db = sqlite3.connect('phones.sqlite')

phones_db.execute('''
CREATE TABLE Phone (
    id int PRIMARY KEY,
    name text,
    constructor text,
    series text,
    os text
)''')

phones_db.commit()

phones_db.execute('''
CREATE TABLE Phys (
    phone int,
    dimx int,
    dimy int,
    dimz int,
    size int,
    weight int,
    colors text,
    is_tactil short,
    moveable_battery short,
    resolution text,
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
    sim_type text,
    charger_type text,
    bluetooth int,
    cell_reception text,
    nfc short,
    gps short,
    memory int,
    memory_upgrade text,
    ram int,
    audio text,
    processor text,
    battery_amp int,
    FOREIGN KEY(phone) REFERENCES Phone(id)
)
''')

phones_db.commit()

phones_db.close()
