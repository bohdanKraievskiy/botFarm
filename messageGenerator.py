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

import random
import requests

import random
import requests

def get_news_templates(template_type):
    # Replace this function with your logic to fetch templates based on the type
    return [(1, "Breaking News: {title} - Read more here: {link}"),
            (2, "Headline: {title}. Details: {link}")] if template_type == 'news_with_description' else \
           [(3, "{title} - {link}"),
            (4, "{title} {link}")]

def fetch_news(used_template_ids):
    # List of available news sources and their APIs
    news_sources = [
        {
            'name': 'New York Times',
            'endpoint': 'https://api.nytimes.com/svc/topstories/v2/home.json',
            'api_key': 'sVRrzlbvV8nYwzRGUOWHhJdVAIXYVYrg',
            'params': {}
        },
        {
            'name': 'The Guardian',
            'endpoint': 'https://content.guardianapis.com/search',
            'api_key': '0bcb6bbb-6262-4f40-8320-d4f0d366e4ad',
            'params': {}
        },
        {
            'name': 'BBC News',
            'endpoint': 'https://bbc-api.vercel.app/latest?lang=english',
            'params': {}
        },
        {
            'name': 'Fox News',
            'endpoint': 'https://riad-news-api.vercel.app/api/news',
            'params': {}
        },
        {
            'name': 'NBC News',
            'endpoint': 'https://newsapi.org/v2/everything?domains=wsj.com&apiKey=3d5b9dcf0d4a4981a0ef655a71bfb32f',
            'params': {}
        },
        {
            'name': 'CBS News',
            'endpoint': 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3d5b9dcf0d4a4981a0ef655a71bfb32f',
            'params': {}
        },
        {
            'name': 'ABC News',
            'endpoint': 'https://newsapi.org/v2/everything?q=apple&from=2024-08-12&to=2024-08-12&sortBy=popularity&apiKey=3d5b9dcf0d4a4981a0ef655a71bfb32f',
            'params': {}
        },
        {
            'name': 'USA Today',
            'endpoint': 'https://newsapi.org/v2/everything?q=tesla&from=2024-07-13&sortBy=publishedAt&apiKey=3d5b9dcf0d4a4981a0ef655a71bfb32f',
            'params': {}
        },
        {
            'name': 'Los Angeles Times',
            'endpoint': 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3d5b9dcf0d4a4981a0ef655a71bfb32f',
            'params': {}
        }
    ]

    # Select a random news source
    source = random.choice(news_sources)
    url = source['endpoint']
    api_key = source.get('api_key')
    params = source.get('params', {})
    if api_key:
        params['apiKey'] = api_key

    # Fetch news from the selected source
    response = requests.get(url, params=params)
    if response.status_code == 200:
        articles = response.json().get('articles', [])  # Adjust based on API response structure
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


    fallback_phrases = [
        "What do you think about the latest news? Check it out!",
        "Couldn't fetch the news right now, but stay tuned for updates!",
        "Stay informed! More news coming your way soon.",
        "Sorry, no news updates available at the moment. Please check back later.",
        "Unable to get the latest news. How about checking out the headlines on your favorite news site?",
        "Our news feed is currently down. Stay tuned for more updates!",
        "News update is unavailable. Make sure to keep yourself informed!",
        "We are experiencing technical difficulties with our news feed. Thank you for your patience!",
        "No news at the moment. Stay tuned!",
        "Stay updated! We'll bring you the news shortly.",
    ]

    return ''


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
