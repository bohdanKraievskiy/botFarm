import sqlite3
import random

def get_random_user():
    conn = sqlite3.connect('./users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT first_name, password, style, topics FROM users ORDER BY RANDOM() LIMIT 1')
    user = cursor.fetchone()
    conn.close()
    if user:
        return user[0], user[1], user[2], user[3].split(',')  # Split topics into a list
    return None


def get_new_random_user():
    conn = sqlite3.connect('./new_users.db')
    cursor = conn.cursor()

    # Витягування всіх записів
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    if not users:
        return None

    user = random.choice(users)

    try:
        first_name = user[1]
        last_name = user[2]
        email = user[3]
        password = user[4]
        bio = user[5]
        style = user[6]
        topics = user[7].split(',')  # Split topics into a list
        message_type = user[8]
        topic = user[9]
        keywords = user[10].split(',')  # Split keywords into a list
    except IndexError as e:
        print(f"Error: {e}")
        print(f"User data: {user}")
        return None

    conn.close()
    return first_name, last_name, email, password, bio, style, topics, message_type, topic, keywords