import sqlite3


def get_random_user():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT first_name, password, style, topics FROM users ORDER BY RANDOM() LIMIT 1')
    user = cursor.fetchone()
    conn.close()
    if user:
        return user[0], user[1], user[2], user[3].split(',')  # Split topics into a list
    return None
