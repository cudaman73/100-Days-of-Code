from config import *
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Firefox(service=Service(WEBDRIVER))
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        self.driver.find_element(By.CLASS_NAME, "js-start-test").click()
        time.sleep(45)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self, up, down):
        message = f"Hey Spectrum, why is my internet speed currently {self.down} down/{self.up} up when I pay for " \
                  f"{down}/{up}? "
        self.driver.get("https://twitter.com/i/flow/login")
        # Have to sleep a bit here because the DOM isn't immediately interactible.
        time.sleep(3)

        # input username and password
        self.driver.find_element(By.CLASS_NAME, "r-30o5oe").send_keys(TWITTER_USER, Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "r-homxoj").send_keys(TWITTER_PASS, Keys.ENTER)
        # wait for page to load once we login, then send angry tweet!
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "public-DraftEditor-content").send_keys(message)
        self.driver.find_element(By.CSS_SELECTOR, "div[data-testid='tweetButtonInline']").click()


complainer = InternetSpeedTwitterBot()

if complainer.up < PROMISED_UP * .9 or complainer.down < PROMISED_DOWN * .9:
    complainer.tweet_at_provider(PROMISED_UP, PROMISED_DOWN)
