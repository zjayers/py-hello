import sqlite3
import json
from pathlib import Path

movies = json.loads(Path('movies.json').read_text())

# Insert into Database
with sqlite3.connect("db.sqlite3") as connection:
    tableCreation = 'CREATE TABLE IF NOT EXISTS Movies(Id INTEGER, Title TEXT, Year INTEGER)'
    connection.execute(tableCreation)
    command = 'INSERT INTO Movies VALUES(?,?,?)'
    for movie in movies:
        connection.execute(command, tuple(movie.values()))
    connection.commit()

# Get From Database
with sqlite3.connect("db.sqlite3") as connection:
    command = 'SELECT * FROM Movies'
    cursor = connection.execute(command)
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)
