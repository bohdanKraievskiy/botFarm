import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scripts.loginScript import login
from scripts.postScript import post_message
from scripts.db_utils import get_random_user
from messageGenerator import generate_message_with_hashtags, fetch_news

# Вказати шлях до драйвера
chrome_driver_path = 'chromedriver-win64/chromedriver.exe'  # Змініть на шлях до вашого ChromeDriver
options = Options()
# Додайте необхідні опції, наприклад headless режим
# options.add_argument("--headless")
service = Service(chrome_driver_path)

def perform_actions_for_user(driver, username, password, style, topics, used_messages, used_template_ids):
    try:
        # Виклик функції логіну
        login(driver, username, password)

        # Очікування переходу на сторінку після входу
        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://chatter.al/home')
        )

        # Визначити, чи публікувати новини
        if random.random() < 0.3:  # 30% ймовірності
            message = fetch_news(used_template_ids)
        else:
            message = generate_message_with_hashtags(style, topics, used_messages)
            if message is None:
                message = fetch_news(used_template_ids)  # Fallback to news if no unique message is found

        post_message(driver, message)

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
    driver = webdriver.Chrome()
    perform_actions_for_user(driver, username, password, style, topics, used_messages, used_template_ids)
    driver.quit()
else:
    print("No users found.")
