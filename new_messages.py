import sqlite3

def init_new_user_db():
    conn = sqlite3.connect('messageTemplates/new_users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            bio TEXT NOT NULL,
            style TEXT NOT NULL,
            topics TEXT NOT NULL,
            message_type TEXT NOT NULL,
            topic TEXT NOT NULL,
            keywords TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def init_new_message_templates_db():
    conn = sqlite3.connect('messageTemplates/new_message_templates.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            style TEXT NOT NULL,
            template TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_template(style, template):
    conn = sqlite3.connect('new_message_templates.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO messages (style, template) VALUES (?, ?)
    ''', (style, template))
    conn.commit()
    conn.close()

# Initialize databases
init_new_user_db()
init_new_message_templates_db()

# Add some example templates (repeat as needed)
add_template('friendly', 'Hey there! What do you think about {topic}?')
add_template('serious', 'Let us discuss the important topic of {topic}.')
add_template('funny', 'Why did the {topic} cross the road? To get to the other side!')
add_template('informal', 'Yo! Check this out: {topic}.')
add_template('educational', 'Did you know about {topic}? It is fascinating.')
add_template('thoughtful', 'Reflecting on {topic}, what are your thoughts?')
# Add more templates as required
