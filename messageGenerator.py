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

# Function to get news templates from database
def get_news_templates(style):
    conn = sqlite3.connect('message_templates.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, template FROM messages WHERE style = ?', (style,))
    templates = cursor.fetchall()
    conn.close()
    return templates

def fetch_news(used_template_ids):
    nytimes_api_key = 'sVRrzlbvV8nYwzRGUOWHhJdVAIXYVYrg'
    url = f'https://api.nytimes.com/svc/topstories/v2/home.json?api-key={nytimes_api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('results', [])
        if articles:
            article = random.choice(articles)
            title = article.get('title', 'News')
            link = article.get('url', '')

            # Get templates with descriptions and only links
            templates_with_description = get_news_templates('news_with_description')
            templates_with_link_only = get_news_templates('news_with_link_only')

            # Choose template style
            if random.random() < 0.7:  # 70% chance for description
                templates = templates_with_description
            else:  # 30% chance for link only
                templates = templates_with_link_only

            # Filter out already used templates
            available_templates = [tpl for tpl in templates if tpl[0] not in used_template_ids]

            if available_templates:
                template_id, template = random.choice(available_templates)
                used_template_ids.add(template_id)
                return template.format(title=title, link=link)

    return ""

def reset_used_template_ids(style):
    conn = sqlite3.connect('message_templates.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM messages WHERE style = ?', (style,))
    template_ids = {row[0] for row in cursor.fetchall()}
    conn.close()
    return template_ids

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
    used_template_ids = set()
    styles = [
        'friendly', 'serious', 'funny', 'formal', 'informal', 'motivational',
        'inspirational', 'educational', 'thoughtful'
    ]
    topics = [
        "music", "movies", "books", "technology", "science", "politics",
        "memes", "jokes", "travel", "food", "fitness", "health", "art",
        "history", "philosophy", "nature", "sports"
    ]
    message_types = ["friendship", "news", "memes", "jokes"]

    for _ in range(10):  # Generate 10 messages for demonstration
        style = random.choice(styles)  # Randomly choose a style
        message = generate_message_with_hashtags(style, topics, used_messages)
        if message:
            print(f"Generated message: {message}")
        else:
            print("No unique message found. Fetching news...")
            news_message = fetch_news(used_template_ids=used_template_ids)
            print(f"News message: {news_message}")
