import sqlite3

con = sqlite3.connect("animegress.db")

cursor = con.cursor()

#create a dummy table
cursor.execute(
    """
               CREATE Table anime (
               name TEXT,
               total_episodes INTEGER,
               genre TEXT
            )
"""
)

Anime_list = [
    ('Attack on Titan', 75, "Action")
    ("Naruto", 225, "Action")
    ("Bleach", 500, "Action")
    ("JoJo's Bizarre Adventure", 52, "Action")
    ("Working!!!", 24, "Comedy")
]

cursor.executemany(
    """
    INSERT into anime (name, total_episodes, genre)
    Values(?, ?, ?)
    """,
    Anime_list
)

con.commit()
