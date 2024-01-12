import sqlite3
import os




Path = os.path.dirname(__file__) + os.sep

con = sqlite3.connect(Path + "students.db")

cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    major TEXT
                )''')















