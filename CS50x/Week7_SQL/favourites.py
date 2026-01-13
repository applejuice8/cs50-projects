from cs50 import SQL

db = SQL('sqlite:///favourites.db')

favourite = input('Favourite: ')

rows = db.execute('SELECT COUNT(*) AS n FROM favourites WHERE language = ?', favourite)

print(rows[0]['n'])


# If no 'BEGIN TRANSACTION', 'COMMIT', race condition
# All code within must be executed together
'''
db.execute('BEGIN TRANSACTION')

rows = db.execute('SELECT likes FROM posts WHERE id = ?', id);
likes = rows[0]['likes']
db.execute('UPDATE posts SET likes = ? WHERE id = ?', likes + 1, id);

db.execute('COMMIT')
'''

# SQL Injection (Case 1)
username = "malan@harvard.edu'--"
password = ''
rows = db.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
rows = db.execute(f"SELECT * FROM users WHERE username = 'malan@harvard.edu'--' AND password = '{password}'")
rows = db.execute(f"SELECT * FROM users WHERE username = 'malan@harvard.edu'")

# SQL Injection (Case 2)
username = "' OR (1 == 1)--"
rows = db.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
rows = db.execute(f"SELECT * FROM users WHERE username = '' OR (1 == 1)--' AND password = '{password}'")
rows = db.execute(f"SELECT * FROM users WHERE username = '' OR (1 == 1)")

# Correct
rows = db.execute(f"SELECT * FROM users WHERE username = ? AND password = ?", username, password)
