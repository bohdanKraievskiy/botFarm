import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scripts.loginScript import login
from scripts.postScript import post_message
from scripts.db_utils import get_all_users
from scripts.messageGenerator import generate_message_with_hashtags, fetch_news

# Вказати шлях до драйвера
chrome_driver_path = 'chromedriver-win64/chromedriver.exe'  # Змініть на шлях до вашого ChromeDriver
options = Options()
service = Service(chrome_driver_path)

def perform_actions_for_user(driver, username, password, style, topics, used_messages):
    try:
        # Виклик функції логіну
        login(driver, username, password)

        # Очікування переходу на сторінку після входу
        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://chatter.al/home')
        )

        message = generate_message_with_hashtags(style, topics, used_messages)
        if message is None:
            message = fetch_news()  # Fallback to news if no unique message is found

        post_message(driver, message)

    except Exception as e:
        print(f"An error occurred for user {username}: {e}")
    finally:
        # Ensure we start fresh for the next user
        driver.delete_all_cookies()

# Отримати всіх користувачів з бази даних
users = get_all_users()
used_messages = set()

for username, password, style, topics in users:
    driver = webdriver.Chrome()
    perform_actions_for_user(driver, username, password, style, topics, used_messages)
    driver.quit()
