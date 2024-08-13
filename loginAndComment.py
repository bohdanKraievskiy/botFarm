import time
import sqlite3
import random
from playwright.sync_api import sync_playwright
from scripts.loginScript import login
from scripts.db_utils import get_random_user
def get_random_comment():
    conn = sqlite3.connect('./message_templates.db')
    cursor = conn.cursor()
    cursor.execute('SELECT template FROM Comments_Templates')
    templates = cursor.fetchall()
    conn.close()
    return random.choice(templates)[0]

def post_comment(page):
    try:
        # Click on the comment button
        comment_button = page.wait_for_selector('//button[contains(@class, "ctrls-item")]/a[contains(@href, "thread")]', timeout=10000)
        comment_button.click()

        # Scroll down to ensure elements are in the viewport
        page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        # Ensure elements are interactable
        time.sleep(2)

        # Locate the reply button by a more specific XPath
        reply_button = page.wait_for_selector('//button[@class="ctrls-item" and contains(@onclick, "SMColibri.pub_reply")]', timeout=40000)
        reply_button.scroll_into_view_if_needed()
        time.sleep(1)
        reply_button.click()

        # Wait for the comment box to appear
        comment_box = page.wait_for_selector('//textarea[@name="post_text"]', timeout=50000)
        time.sleep(1)
        comment_box.fill(get_random_comment())

        # Submit the comment
        publish_button = page.wait_for_selector('//button[contains(text(),"Publish")]', timeout=50000)
        time.sleep(1)
        publish_button.click()

        print("Successfully posted a comment!")
    except Exception as e:
        print(f"An error occurred while posting a comment: {e}")

def perform_actions_for_user(username, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Set headless=True to run without UI
        page = browser.new_page()

        # Log in the user
        page.goto('https://chatter.al/guest')
        page.fill('input[name="email"]', username)
        page.fill('input[name="password"]', password)
        page.click('button.btn.btn-custom.main-inline.lg.btn-block')

        # Wait for the home page to load
        page.wait_for_url('https://chatter.al/home')
        page.goto('https://chatter.al/search')

        # Post a comment on the latest post
        post_comment(page)

        browser.close()

# Get a random user from the database
random_user = get_random_user()
if random_user:
    username, password, style, topics = random_user
    perform_actions_for_user(username, password)
