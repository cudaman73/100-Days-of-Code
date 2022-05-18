from config import LINKEDIN_URL, PATH_TO_DRIVER, USERNAME, PASSWORD
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(service=Service(PATH_TO_DRIVER))
driver.get(LINKEDIN_URL)

sign_in = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_in.click()

time.sleep(5)

login_email = driver.find_element(By.ID, "username")
login_email.send_keys(USERNAME)

login_password = driver.find_element(By.ID, "password")
login_password.send_keys(PASSWORD)

login_button = driver.find_element(By.TAG_NAME)