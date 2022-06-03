from config import ZILLOW_URL, FORM_URL, PATH_TO_DRIVER
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(service=Service(PATH_TO_DRIVER))
driver.get(ZILLOW_URL)

time.sleep(1)

# scroll to bottom of page so all elements are loaded
elem = driver.find_element(By.ID, "search-page-list-container")

no_pagedowns = 15

while no_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_pagedowns -= 1

# there are duplicate links returned, so we filter them using list comprehension
link_elements = driver.find_elements(By.CSS_SELECTOR, 'li > article > div > a')
links = []
[links.append(x.get_attribute("href")) for x in link_elements if x.get_attribute('href') not in links]

addresses = [x.text for x in driver.find_elements(By.CLASS_NAME, 'list-card-addr')]
# strip '/mo' from pricing text
prices = [x.text.split("/")[0] for x in driver.find_elements(By.CLASS_NAME, 'list-card-price')]

driver.get(FORM_URL)
for x in range(len(addresses)):
    inputs = driver.find_elements(By.CLASS_NAME, 'whsOnd')
    inputs[0].send_keys(addresses[x])
    inputs[1].send_keys(prices[x])
    inputs[2].send_keys(links[x])

    submit_button = driver.find_element(By.CLASS_NAME, 'l4V7wb')
    submit_button.click()

    repeat_link = driver.find_element(By.LINK_TEXT, 'Submit another response')
    repeat_link.click()
