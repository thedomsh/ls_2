import sqlite3

database = sqlite3.connect('hw.db')

cursor = database.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS weather(
    city TEXT,
    temperature TEXT,
    wind_speed TEXT,
    humidity TEXT,
    day_temp TEXT
)
''')

database.commit()
database.close()
