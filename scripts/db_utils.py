import sqlite3

def get_all_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT first_name, password, style, topics FROM users')
    users = cursor.fetchall()
    conn.close()
    return [(user[0], user[1], user[2], user[3].split(',')) for user in users]  # Split topics into a list
