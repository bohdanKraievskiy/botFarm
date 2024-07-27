from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import random
from selenium.webdriver.support import expected_conditions as EC
from scripts.loginScript import login
from scripts.postScript import post_message_gif
from scripts.db_utils import get_random_user
from messageGenerator import generate_message,generate_message_with_hashtags, fetch_news
from webdriver_manager.chrome import ChromeDriverManager

# Вказати шлях до драйвера
chrome_driver_path = '/usr/local/bin/chromedriver'  # Змініть на шлях до вашого ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
service = ChromeService(executable_path=ChromeDriverManager().install())


def perform_actions_for_user(driver, username, password, style, topics, used_messages, used_template_ids):
    try:
        # Виклик функції логіну
        login(driver, username, password)

        # Очікування переходу на сторінку після входу
        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://chatter.al/home')
        )
        message = generate_message(style, topics, used_messages)
        topic = random.choice(topics)
        print(topic)
        post_message_gif(driver, message, topic)
        print("Posted successfully! User - " + username)
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