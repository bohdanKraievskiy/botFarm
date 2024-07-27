import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scripts.loginScript import login
from scripts.bioScript import generate_bio
from scripts.bioScript import change_bio
from scripts.bioScript import user_has_bio
from scripts.db_utils import get_random_user
from messageGenerator import generate_message_with_hashtags, fetch_news
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_path = '/usr/local/bin/chromedriver'  # Змініть на шлях до вашого ChromeDriver
options = webdriver.ChromeOptions()

service = ChromeService(executable_path=ChromeDriverManager().install())

def perform_actions_for_user(driver, username, password, style, topics, used_messages, used_template_ids):
    try:
        # Виклик функції логіну
        login(driver, username, password)

        # Очікування переходу на сторінку після входу
        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://chatter.al/home')
        )
        if not user_has_bio(username):
          new_bio = generate_bio(topics)
          print(f"Bio generated: {new_bio}")
          change_bio(driver, new_bio,username)
          print(f"Bio changed to: {new_bio}")
        else:
          print(f"User {username} already has a bio.")
    except Exception as e:
        print(f"An error occurred for user {username}: {e}")
    finally:
        # Ensure we start fresh for the next user
        driver.delete_all_cookies()

# Отримати одного випадкового користувача з бази даних
used_messages = set()
used_template_ids = set()

random_user = get_random_user()
if random_user:
    username, password, style, topics = random_user
    driver = webdriver.Chrome(service=service, options=options)
    perform_actions_for_user(driver, username, password, style, topics, used_messages, used_template_ids)
    driver.quit()
else:
    print("No users found.")