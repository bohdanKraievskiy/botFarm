import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scripts.loginScript import login
from scripts.db_utils import get_random_user
from scripts.profilePhotoScript import change_profile_photo
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

        # Зміна фото профілю
        change_profile_photo(driver, username)
        print(f"Profile photo changed for user: {username}")

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
