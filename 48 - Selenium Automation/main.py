from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

driver_path = path_to_driver
service = Service(driver_path)
driver = webdriver.Firefox(service=service)

driver.get("https://www.python.org/")
date_tags = driver.find_element(By.CLASS_NAME, "shrubbery").find_elements(By.TAG_NAME, 'time')
event_tags = driver.find_element(By.CLASS_NAME, "shrubbery").find_elements(By.TAG_NAME, 'a')

events = {}

for x in range(len(date_tags)):
    date = date_tags[x].text.split('T')[0]
    name = event_tags[x].text
    events.update({f'{x}': {'time': f'{date}', 'name': f'{name}'}})

print(events)

driver.quit()
