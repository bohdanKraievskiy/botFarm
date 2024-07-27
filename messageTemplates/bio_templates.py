import sqlite3
import os


def add_bio_templates():
    # Определяем путь к файлу базы данных
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'message_templates.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Создаем таблицу bio_templates, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bio_templates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            template TEXT NOT NULL
        )
    ''')


    templates = [
        "Exploring life's mysteries one day at a time. Passionate about learning new things and connecting with others who share the same curiosity.",
        "Always eager to dive into new experiences and broaden my horizons. Let’s connect and inspire each other through thoughtful conversations.",
        "Driven by a love for creativity and self-expression. I enjoy engaging in discussions that spark new ideas and bring out the best in everyone.",
        "Looking for authentic connections and meaningful conversations. Let’s explore the world together and share our unique perspectives and insights.",
        "Focused on personal growth and the journey of self-discovery. I believe in the power of sharing experiences and learning from each other.",
        "Creative spirit with a passion for innovation and exploration. Let’s discuss ideas and collaborate on projects that make a difference in our lives.",
        "Genuine and thoughtful, always ready for a deep conversation or a light-hearted chat. Let’s connect and see where our conversations take us.",
        "Enthusiastic about finding new ways to learn and grow. I’m here to share my experiences and learn from yours in an open and engaging way.",
        "Passionate about connecting with people from all walks of life. Let’s share stories, discuss ideas, and build meaningful relationships together.",
        "Optimistic and driven, with a love for exploring new ideas and opportunities. I enjoy connecting with others who have a positive outlook on life.",
        "Dedicated to understanding different perspectives and building connections with others. Let’s have conversations that challenge and inspire us.",
        "Curious about the world and eager to learn from others. I believe in the power of conversation to spark new ideas and foster personal growth.",
        "Inspired by creativity and the beauty of diverse viewpoints. Let’s connect and explore new ideas together, sharing our passions and experiences.",
        "Focused on making the most of every opportunity to learn and grow. I’m here to engage in meaningful discussions and connect with like-minded individuals.",
        "Always ready for a thought-provoking conversation and a chance to connect with others. Let’s explore new ideas and support each other’s journeys.",
        "Driven by a desire to understand the world and connect with others. I enjoy having deep conversations and exploring new perspectives with those around me.",
        "Eager to build relationships and share experiences with others. Let’s have discussions that are both enlightening and enjoyable, and inspire each other.",
        "Passionate about exploring new ideas and connecting with people who share similar interests. I believe in the power of conversation to create change.",
        "Creative thinker who loves engaging in discussions that spark new ideas and insights. Let’s connect and see how our conversations can make an impact.",
        "Reflective and open-minded, committed to learning from others and sharing my own experiences. Let’s build connections through meaningful conversations."
    ]

    cursor.executemany('INSERT INTO bio_templates (template) VALUES (?)', [(t,) for t in templates])
    conn.commit()
    conn.close()


if __name__ == "__main__":
    add_bio_templates()
