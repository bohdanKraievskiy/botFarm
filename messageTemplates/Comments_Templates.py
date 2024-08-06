import sqlite3

def create_comments_table():
    conn = sqlite3.connect('../message_templates.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Comments_Templates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            template TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def populate_comment_templates():
    conn = sqlite3.connect('../message_templates.db')
    cursor = conn.cursor()
    templates = [
        "Great post! Thanks for sharing.",
        "I completely agree with you.",
        "Interesting perspective!",
        "Thanks for the info!",
        "Looking forward to more posts like this.",
        "This is very insightful.",
        "Couldn't have said it better myself.",
        "Keep up the good work!",
        "I learned something new today.",
        "Thanks for the great content!"
    ]
    cursor.executemany('INSERT INTO Comments_Templates (template) VALUES (?)', [(template,) for template in templates])
    conn.commit()
    conn.close()

import random

# Example usage
if __name__ == "__main__":
    create_comments_table()
