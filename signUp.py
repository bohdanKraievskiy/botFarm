from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from scripts.signUpScript import register, init_db

# Example usage:
chrome_driver_path = './chromedriver-win64/chromedriver.exe'  # Змініть на шлях до вашого ChromeDriver
options = Options()
# Add any Chrome options you need here, for example:
# options.add_argument('--headless')  # Example: running in headless mode if needed
service = Service(chrome_driver_path)
driver = webdriver.Chrome()

conn = init_db()

try:
    register(driver, conn)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    conn.close()
