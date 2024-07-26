from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from scripts.signUpScript import register, init_db
from webdriver_manager.chrome import ChromeDriverManager
# Example usage:
chrome_driver_path = '/usr/local/bin/chromedriver'  # Змініть на шлях до вашого ChromeDriver

options = webdriver.ChromeOptions()
# Add any Chrome options you need here, for example:
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

conn = init_db()

try:
    register(driver, conn)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    conn.close()
