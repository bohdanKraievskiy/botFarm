import random
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scripts.loginScript import login
from scripts.postScript import post_message
from scripts.db_utils import get_new_random_user
from webdriver_manager.chrome import ChromeDriverManager


def perform_actions_for_user(driver, username, password, style, topics, used_messages, used_template_ids):
    try:
        login(driver, username, password)
        WebDriverWait(driver, 10).until(EC.url_to_be('https://chatter.al/home'))

        # Wait for the home page to load
        WebDriverWait(driver, 20).until(
            EC.url_to_be('https://chatter.al/home')
        )

        # Navigate to the desired page
        driver.get('https://chatter.al/search')

        # Wait for the button to be visible and clickable
        like_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@onclick=\"SMColibri.like_post('2417', this);\"]"))
        )

        # Scroll to the button
        driver.execute_script("arguments[0].scrollIntoView(true);", like_button)

        # Click the button
        like_button.click()

    except Exception as e:
        print(f"An error occurred for user {username}: {e}")
    finally:
        driver.delete_all_cookies()


options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
service = ChromeService(executable_path=ChromeDriverManager().install())

used_messages = set()
used_template_ids = set()

for attempt in range(10):
    random_user = get_new_random_user()
    if random_user:
        first_name, last_name, email, password, bio, style, topics, message_type, topic, keywords = random_user
        driver = webdriver.Chrome(service=service, options=options)
        perform_actions_for_user(driver, first_name,password, style, topics, used_messages, used_template_ids)
        driver.quit()
    else:
        print("No users found.")
        break  # Exit the loop if no more users are available
