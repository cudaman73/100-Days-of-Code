from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
import keyboard

driver_path = path_to_driver
service = Service(driver_path)
driver = webdriver.Firefox(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")


def click_on_cookie(num):
    big_cookie = driver.find_element(By.ID, "bigCookie")
    for i in range(num):
        big_cookie.click()


def check_for_upgrade():
    upgrades = driver.find_elements(By.CSS_SELECTOR, "[class='crate upgrade enabled']")
    for x in reversed(upgrades):
        print(f"can afford {x.id}")
        x.click()
    upgrades = driver.find_elements(By.CSS_SELECTOR, "[class='product unlocked enabled']")
    for x in reversed(upgrades):
        print(f"can afford {x.find_element(By.CSS_SELECTOR, 'div.title').text}")
        x.click()


# time to wait for the site to load
time.sleep(5)

while True:
    click_on_cookie(1)
    check_for_upgrade()

    # Kill switch
    if keyboard.is_pressed("q"):
        break

# driver.quit()
