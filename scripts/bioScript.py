import time
import sqlite3
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_bio_template():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'message_templates.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT template FROM bio_templates ORDER BY RANDOM() LIMIT 1')
    template = cursor.fetchone()
    conn.close()
    return template[0] if template else None

def generate_bio(topics):
    template = get_bio_template()
    if template:
        bio = template.format(topics=', '.join(topics))
        return bio if len(bio) <= 140 else bio[:140]
    return ""
def login(driver, username, password):
    driver.get('https://chatter.al/guest')

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'email'))
    )
    password_input = driver.find_element(By.NAME, 'password')

    email_input.send_keys(username)
    password_input.send_keys(password)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Login")]'))
    )
    login_button.click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be('https://chatter.al/home')
    )

def change_bio(driver, new_bio,username):
    driver.get('https://chatter.al/settings/bio')
    WebDriverWait(driver, 40).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, 'main-preloader'))
    )	
    bio_textarea = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'bio'))
    )
    bio_textarea.clear()
    bio_textarea.send_keys(new_bio)

    save_button = driver.find_element(By.XPATH, '//button[contains(text(), "Save changes")]')
    driver.execute_script("arguments[0].click();", save_button)
    save_bio_to_db(username, new_bio)
    time.sleep(3)
# Save generated bio to the database
def save_bio_to_db(username, bio):
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'users.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET bio = ? WHERE first_name = ?', (bio, username))
    conn.commit()
    conn.close()
def user_has_bio(username):
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'users.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT bio FROM users WHERE first_name = ?', (username,))
    bio = cursor.fetchone()
    conn.close()
    return bio and bio[0]
if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_service = Service('path/to/chromedriver')

    driver = webdriver.Chrome()

    try:
        username = 'Dione'  # Замініть на ваш email або ім'я користувача
        password = 'woABp)X'  # Замініть на ваш пароль

        login(driver, username, password)

        if not user_has_bio(username):
            topics = ["music", "movies", "books"]  # Замініть на фактичні теми користувача
            new_bio = generate_bio(topics)
            change_bio(driver, new_bio)
            print(f"Bio changed to: {new_bio}")
        else:
            print(f"User {username} already has a bio.")
    finally:
        driver.quit()
