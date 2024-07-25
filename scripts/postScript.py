import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def post_message(driver, message):
    post_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "timeline-pubbox__textinput")]//textarea'))
    )
    post_box.send_keys(message)

    publish_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'//button[contains(text(),"Publish")]'))
    )
    publish_button.click()

    time.sleep(5)  # Wait for the post to be published
