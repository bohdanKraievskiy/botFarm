import time
from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def post_message_gif(driver, message, topic):
    post_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "timeline-pubbox__textinput")]//textarea'))
    )
    post_box.send_keys(message)
    time.sleep(5)  # Wait for the post to be published
    post_with_gif(driver, topic)
    time.sleep(5)  # Wait for the post to be published

    publish_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Publish")]'))
    )
    driver.execute_script("arguments[0].click();", publish_button)

    time.sleep(5)  # Wait for the post to be published
def post_message(driver, message):
    post_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "timeline-pubbox__textinput")]//textarea'))
    )
    post_box.send_keys(message)
    time.sleep(5)  # Wait for the post to be published

    publish_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Publish")]'))
    )
    driver.execute_script("arguments[0].click();", publish_button)

    time.sleep(5)  # Wait for the post to be published
def post_with_gif(driver, keyword):
    print("searching for gif button...")
    # Натискаємо кнопку для відкриття гіфок
    gif_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    '#vue-pubbox-app-1 > div > div.timeline-pubbox__footer > div.timeline-pubbox__footer-topline > button:nth-child(7) > svg'))
    )
    gif_button.click()
    print("gif button clicked")
    # Знайти елемент пошуку та ввести ключове слово
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        '#vue-pubbox-app-1 > div > div.timeline-pubbox__body > div.timeline-pubbox__gifs > div > div > div.pubbox-gifs__loader-searchbar > div.searchbar-input > input'))
    )
    search_input.send_keys(keyword)

    # Зачекати 5 секунд для завантаження результатів
    time.sleep(5)

    # Горнути список гіфок на випадковий проміжок часу
    gif_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        '#vue-pubbox-app-1 > div > div.timeline-pubbox__body > div.timeline-pubbox__gifs > div > div > div.pubbox-gifs__loader-list'))
    )
    random_scroll_time = random.uniform(1, 3)
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", gif_list)
    time.sleep(random_scroll_time)

    # Вибрати та натиснути на випадкову гіфку
    gifs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                             '#vue-pubbox-app-1 > div > div.timeline-pubbox__body > div.timeline-pubbox__gifs > div > div > div.pubbox-gifs__loader-list img'))
    )
    random_gif = random.choice(gifs)
    random_gif.click()

    time.sleep(2)