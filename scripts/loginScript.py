import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    # Перехід на сторінку входу
    driver.get('https://chatter.al/guest')

    # Знаходження полів вводу логіну та паролю та їх заповнення
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'email'))
    )
    password_input = driver.find_element(By.NAME, 'password')

    email_input.send_keys(username)  # Замініть на ваш email або ім'я користувача
    password_input.send_keys(password)  # Замініть на ваш пароль
       # Очікування зникнення блокуючого елемента
    WebDriverWait(driver, 40).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, 'main-preloader'))
    )
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Login")]'))
    )
    login_button.click()

    # Очікування переходу на сторінку після входу
    WebDriverWait(driver, 10).until(
        EC.url_to_be('https://chatter.al/home')
    )
