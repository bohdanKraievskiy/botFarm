import os
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from scripts.loginScript import login


def get_random_photo_url():
    # Використовуємо Lorem Picsum для отримання випадкового зображення
    return 'https://picsum.photos/400/400'

def download_photo(photo_url, photo_path):
    response = requests.get(photo_url)
    if response.status_code == 200:
        with open(photo_path, 'wb') as file:
            file.write(response.content)
    else:
        raise Exception("Failed to download the photo")
def change_profile_photo(driver, username):
    driver.get(f'https://chatter.al/{username}')

    # Очікування зникнення блокуючого елемента
    WebDriverWait(driver, 60).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, 'main-preloader'))
    )

    try:
        # Спочатку знайдемо всі кнопки з класом "profile-avatar"
        avatar_buttons = driver.find_elements(By.XPATH, '//*[@id="vue-profile-cover-app"]/div[3]')

        # Потім знайдемо шапку профілю
        profile_header = driver.find_element(By.XPATH, '//*[@id="vue-profile-cover-app"]/div[1]')
        upload_button = None
        # Виберемо кнопку, яка не є дочірнім елементом шапки профілю
        for button in avatar_buttons:
            if not profile_header in button.find_elements(By.XPATH,
                                                          './ancestor::div[@id="vue-profile-cover-app"]/div[1]'):
                upload_button = button
                break

        if upload_button:
            # Прокрутка до кнопки профілю перед натисканням
            driver.execute_script("arguments[0].scrollIntoView(true);", upload_button)

            # Використання JavaScript для натискання
            driver.execute_script("arguments[0].click();", upload_button)
        else:
            print("Відповідну кнопку не знайдено.")

    except Exception as e:
        print("Error finding upload button:", e)
        raise

    print("Clicked upload button")

    upload_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="file"]'))
    )

    # Завантажити випадкове зображення
    photo_url = get_random_photo_url()
    photo_path = os.path.join(os.path.dirname(__file__), 'random_photo.jpg')

    download_photo(photo_url, photo_path)
    upload_input.send_keys(photo_path)

    save_button = driver.find_element(By.XPATH, '//button[contains(text(), "Save changes")]')
    driver.execute_script("arguments[0].click();", save_button)

    # Очікування збереження змін
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, f'//img[@src="{photo_url}"]'))
    )

    # Додати паузу, щоб переконатися, що процес завершився
    time.sleep(5)

    os.remove(photo_path)  # Видалити завантажене зображення після використання


if __name__ == "__main__":
    options = Options()
    service = ChromeService(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome()

    try:
        username = 'Lyubomir'  # Замініть на ваш email або ім'я користувача
        password = '_qUxC*:Upym6'  # Замініть на ваш пароль

        login(driver, username, password)
        change_profile_photo(driver, username)
        print(f"Profile photo changed for user {username}")

    except Exception as e:
        print(f"An error occurred for user {username}: {e}")

    finally:
        driver.quit()
