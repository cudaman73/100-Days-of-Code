from config import *
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Firefox(service=Service(WEBDRIVER))
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        self.driver.find_element(By.CLASS_NAME, "js-start-test").click()
        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self, up, down):
        pass


complainer = InternetSpeedTwitterBot()

complainer.get_internet_speed()

# if complainer.up < PROMISED_UP or complainer.down < PROMISED_DOWN:
#     complainer.tweet_at_provider(PROMISED_UP, PROMISED_DOWN)
