from config import LINKEDIN_URL, PATH_TO_DRIVER, USERNAME, PASSWORD
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# initialize and grab the job search
driver = webdriver.Firefox(service=Service(PATH_TO_DRIVER))
driver.get(LINKEDIN_URL)

sign_in = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_in.click()

# mild wait because url loads some javascript, which takes some time
# should we change this to an assert to make sure the page is loaded?
time.sleep(3)

login_email = driver.find_element(By.ID, "username")
login_email.send_keys(USERNAME)

login_password = driver.find_element(By.ID, "password")
login_password.send_keys(PASSWORD)

login_button = driver.find_element(By.CSS_SELECTOR, "div > button[type='submit']")
login_button.click()

time.sleep(3)


# here, we could apply to jobs, since we searched for 'easy apply', but instead i want to save
# jobs and follow the company instead, as I don't want to randomly apply for jobs at this point

# minimize the chat list because we can't click on elements behind it.
minimize_button = driver.find_element(By.CSS_SELECTOR, "button > li-icon[type='chevron-down-icon']")
minimize_button.click()

job_list = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")

for job in job_list:

    # click the job listing so that the right pane updates with the listing information
    container = job.find_element(By.CLASS_NAME, "job-card-container")
    container.click()
    time.sleep(2)

    save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save_button.click()
    # navigate to end of page so follow button loads
    save_button.send_keys(Keys.END)
    time.sleep(2)
    save_button.send_keys(Keys.END)
    time.sleep(2)

    follow_button = driver.find_element(By.CLASS_NAME, "follow")
    follow_button.click()
