import time
import random
import string
import requests
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Database setup
def init_db():
    conn = sqlite3.connect('./new_users.db')
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
    return conn

def save_user_to_db(conn, first_name, last_name, email, password, bio, style, topics, message_type, topic, keywords):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (first_name, last_name, email, password, bio, style, topics, message_type, topic, keywords)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, email, password, bio, style, ','.join(topics), message_type, topic, ','.join(keywords)))
    conn.commit()

def generate_random_user():
    response = requests.get('https://randomuser.me/api/')
    user_data = response.json()['results'][0]
    first_name = user_data['name']['first']
    last_name = user_data['name']['last']
    email = user_data['email']
    styles = [
        'friendly', 'serious', 'funny', 'formal', 'informal', 'motivational',
        'inspirational', 'educational', 'thoughtful'
    ]
    topics = {
        "music": ["melody", "harmony", "rhythm"],
        "movies": ["cinema", "director", "film"],
        "books": ["literature", "novel", "author"],
        "technology": ["innovation", "software", "AI"],
        "science": ["experiment", "research", "theory"],
        "politics": ["government", "policy", "election"],
        "memes": ["viral", "funny", "internet"],
        "jokes": ["humor", "laugh", "funny"],
        "travel": ["adventure", "journey", "explore"],
        "food": ["cuisine", "recipe", "delicious"],
        "fitness": ["workout", "exercise", "health"],
        "health": ["wellness", "nutrition", "medicine"],
        "art": ["painting", "sculpture", "creativity"],
        "history": ["past", "event", "chronicle"],
        "philosophy": ["thought", "wisdom", "theory"],
        "nature": ["environment", "wildlife", "ecosystem"],
        "sports": ["game", "competition", "team"]
    }

    style = random.choice(styles)
    selected_topic = random.choice(list(topics.keys()))
    selected_keywords = topics[selected_topic]
    message_type = random.choice(["friendship", "news", "memes", "jokes"])

    return first_name, last_name, email, style, selected_topic, selected_keywords, message_type

def generate_random_text():
    response = requests.get('https://baconipsum.com/api/?type=meat-and-filler&sentences=5')
    sentences = response.json()
    text = ''
    for sentence in sentences:
        if 5 <= len(text) + len(sentence) <= 140:
            text += ' ' + sentence
        else:
            break
    return text.strip()

def generate_random_password(min_length=6, max_length=20):
    length = random.randint(min_length, max_length)
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def register(driver, conn):
    first_name, last_name, email, style, topic, keywords, message_type = generate_random_user()
    password = generate_random_password()
    bio = generate_random_text()

    driver.get('https://chatter.al/guest?auth=signup')

    uname_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'uname'))
    )
    email_input = driver.find_element(By.NAME, 'email')
    password_input = driver.find_element(By.NAME, 'password')
    tos_agree_checkbox = driver.find_element(By.ID, 'tos-agree')
    signup_button = driver.find_element(By.XPATH, '//button[contains(text(),"Sign up")]')

    uname_input.send_keys(first_name)
    email_input.send_keys(email)
    password_input.send_keys(password)
    tos_agree_checkbox.click()
    driver.execute_script("arguments[0].click();", signup_button)

    save_user_to_db(conn, first_name, last_name, email, password, bio, style, [topic], message_type, topic, keywords)

    # Очікування зникнення блокуючого елемента
    WebDriverWait(driver, 40).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, 'main-preloader'))
    )

    # Очікування і натискання кнопки через JavaScript
    skip_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Skip and continue")]'))
    )
    time.sleep(2)
    driver.execute_script("arguments[0].click();", skip_button)

    # Fill profile details
    lname_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'lname'))
    )
    bio_input = driver.find_element(By.NAME, 'bio')
    country_dropdown = driver.find_element(By.XPATH,
                                           '//button[@data-toggle="dropdown" and contains(text(), "United States")]')

    lname_input.send_keys(last_name)
    bio_input.send_keys(bio)

    country_dropdown.click()
    random_country = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@class="dropdown-item" and contains(text(), "United States")]'))
    )
    random_country.click()

    save_and_continue_button = driver.find_element(By.XPATH, '//button[contains(text(), "Save and continue")]')
    driver.execute_script("arguments[0].click();", save_and_continue_button)


