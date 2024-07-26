import sqlite3


def insert_templates_into_db(templates):
    conn = sqlite3.connect('message_templates.db')
    cursor = conn.cursor()

    # Переконайтесь, що таблиця існує
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            style TEXT NOT NULL,
            template TEXT NOT NULL
        )
    ''')

    for style, templates_list in templates.items():
        for template in templates_list:
            cursor.execute('INSERT INTO messages (style, template) VALUES (?, ?)', (style, template))

    conn.commit()
    conn.close()


templates = {
    'friendly': [
        "Hey there! Anyone into {topic}? I've been really enjoying it lately and would love to chat about it.",
        "What's up everyone? Let's talk about {topic}. It's always interesting to hear different perspectives.",
        "Hello friends! Anyone want to chat about {topic}? I think it's such a fascinating topic.",
        "Looking for some good conversation about {topic}. Who's in?",
        "Hi all! What do you think about {topic}? I'd love to know your thoughts."
    ],
    'serious': [
        "Let's have a serious discussion about {topic}. It's a crucial issue that we need to address.",
        "What are the implications of {topic}? This topic has far-reaching consequences.",
        "Can we delve deep into the topic of {topic}? There's so much to uncover.",
        "A critical analysis of {topic} is needed. Let's explore it together.",
        "Let's consider the impact of {topic}. It's something we should all think about."
    ],
    'funny': [
        "Why did the chicken talk about {topic}? To get to the other side of the debate!",
        "What's the deal with {topic}? It's always good for a laugh.",
        "Ever heard a joke about {topic}? It might be the funniest thing you'll hear today.",
        "Let's have a laugh about {topic}. Humor makes everything better.",
        "Why don't we joke around about {topic}? It's a great way to lighten the mood."
    ],
    'formal': [
        "Could we discuss the topic of {topic}? It's an important issue.",
        "May I inquire about your thoughts on {topic}? Your opinion matters.",
        "Let's have a formal discussion about {topic}. It's a significant subject.",
        "What is your perspective on {topic}? I'd like to hear your view.",
        "Can we engage in a conversation about {topic}? It's worth discussing."
    ],
    'motivational': [
        "Believe in yourself and all that you are. Let's talk about how {topic} can inspire us.",
        "The future belongs to those who believe in the beauty of their dreams. How does {topic} play a role in your dreams?",
        "Every day is a new beginning. Take a deep breath, smile, and start again. How does {topic} inspire you to start fresh?",
        "The only limit to our realization of tomorrow is our doubts of today. Let's discuss how {topic} helps overcome those doubts.",
        "Your only limit is your mind. How does {topic} challenge and inspire you to think bigger?"
    ],
    'inspirational': [
        "The best way to predict the future is to create it. Let's talk about how {topic} is shaping the future.",
        "Don't watch the clock; do what it does. Keep going. How does {topic} motivate you to keep moving forward?",
        "Success is not the key to happiness. Happiness is the key to success. How does {topic} bring happiness to your life?",
        "What lies behind us and what lies before us are tiny matters compared to what lies within us. How does {topic} bring out the best in you?",
        "Start where you are. Use what you have. Do what you can. How does {topic} inspire you to take action?"
    ],
    'educational': [
        "Learning never exhausts the mind. Let's discuss how {topic} can broaden our knowledge.",
        "Education is the most powerful weapon which you can use to change the world. How does {topic} contribute to our understanding?",
        "The beautiful thing about learning is that no one can take it away from you. How has {topic} enriched your life?",
        "Education is not the filling of a pail, but the lighting of a fire. How does {topic} ignite your passion for learning?",
        "The more that you read, the more things you will know. How does {topic} expand your horizons?"
    ],
    'thoughtful': [
        "The unexamined life is not worth living. Let's ponder the deeper meaning of {topic}.",
        "To think is easy. To act is hard. But the hardest thing in the world is to act in accordance with your thinking. How does {topic} challenge your beliefs?",
        "The mind is everything. What you think you become. How has {topic} shaped your thoughts?",
        "The only true wisdom is in knowing you know nothing. How does {topic} humble you and inspire growth?",
        "In the end, we will remember not the words of our enemies, but the silence of our friends. How does {topic} impact your perspective on life?"
    ]
}

insert_templates_into_db(templates)
