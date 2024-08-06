import time
import sqlite3
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scripts.loginScript import login
from scripts.db_utils import get_random_user
from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriver setup
chrome_driver_path = 'chromedriver-win64/chromedriver.exe'  # Update to your path
options = Options()

service = ChromeService(executable_path=ChromeDriverManager().install())

def get_random_comment():
    conn = sqlite3.connect('./message_templates.db')
    cursor = conn.cursor()
    cursor.execute('SELECT template FROM Comments_Templates')
    templates = cursor.fetchall()
    conn.close()
    return random.choice(templates)[0]

def post_comment(driver):
    try:

        # Click on the comment button
        comment_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "ctrls-item")]/a[contains(@href, "thread")]'))
        )
        driver.execute_script("arguments[0].click();", comment_button)

        # Scroll down to ensure elements are in the viewport
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Wait for 3 seconds to ensure elements are loaded
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Wait for 3 seconds to ensure elements are loaded again

        # Ensure elements are interactable
        time.sleep(2)

        # Locate the reply button by a more specific XPath
        reply_button = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[@class="ctrls-item" and contains(@onclick, "SMColibri.pub_reply")]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", reply_button)
        time.sleep(1)

        # Click the reply button using JavaScript to avoid "element not interactable" issue
        driver.execute_script("arguments[0].click();", reply_button)

        # Wait for the comment box to appear
        comment_box = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, '//textarea[@name="post_text"]'))
        )
        time.sleep(1)
        comment_box.send_keys(get_random_comment())

        # Submit the comment
        publish_button = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Publish")]'))
        )
        time.sleep(1)
        driver.execute_script("arguments[0].click();", publish_button)

        print("Successfully posted a comment!")
    except Exception as e:
        print(f"An error occurred while posting a comment: {e}")

def perform_actions_for_user(driver, username, password):
    try:
        # Log in the user
        login(driver, username, password)

        # Wait for the home page to load
        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://chatter.al/home')
        )
        driver.get('https://chatter.al/search')
        # Post a comment on the latest post
        post_comment(driver)

    except Exception as e:
        print(f"An error occurred for user {username}: {e}")
    finally:
        # Ensure we start fresh for the next user
        driver.delete_all_cookies()

# Get a random user from the database
random_user = get_random_user()
if random_user:
    username = "Lyubomir"
    password = "_qUxC*:Upym6"
    driver = webdriver.Chrome(service=service, options=options)
    perform_actions_for_user(driver, username, password)
    driver.quit()
