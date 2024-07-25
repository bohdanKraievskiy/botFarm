import random
import sqlite3
import requests


# Database connection
def get_message_templates(style):
    conn = sqlite3.connect('message_templates.db')
    cursor = conn.cursor()
    cursor.execute('SELECT template FROM messages WHERE style = ?', (style,))
    templates = cursor.fetchall()
    conn.close()
    return [template[0] for template in templates]


# Fetch news from The New York Times
def fetch_news():
    nytimes_api_key = 'YOUR_NYTIMES_API_KEY'
    url = f'https://api.nytimes.com/svc/topstories/v2/home.json?api-key={nytimes_api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('results', [])
        if articles:
            article = random.choice(articles)
            title = article.get('title', 'News')
            link = article.get('url', '')
            return f"Have you seen the latest news? {title}. Read more here: {link}"
    return "Check out the latest news on The New York Times!"


# Generate a unique message
def generate_message(style, topics, used_messages):
    templates = get_message_templates(style)
    while templates:
        template = random.choice(templates)
        topic = random.choice(topics)  # Select a random topic from the user's topics
        message = template.format(topic)
        if message not in used_messages:
            used_messages.add(message)
            return message
        templates.remove(template)
    return None


# Generate a message with hashtags
def generate_message_with_hashtags(style, topics, used_messages):
    message = generate_message(style, topics, used_messages)
    if message:
        hashtags = ['#news', '#fun', '#discussion', '#chat']
        if random.random() > 0.3:  # 70% chance to add hashtags
            message += ' ' + ' '.join(random.sample(hashtags, random.randint(1, 3)))
    return message


# Example usage
if __name__ == "__main__":
    used_messages = set()
    styles = ['friendly', 'serious', 'funny', 'formal']
    topics = ["music", "movies", "books", "technology", "science", "politics", "memes", "jokes"]

    for _ in range(10):  # Generate 10 messages for demonstration
        style = random.choice(styles)
        message = generate_message_with_hashtags(style, topics, used_messages)
        print(message)

    # Fetch news example
    news_message = fetch_news()
    print(news_message)
