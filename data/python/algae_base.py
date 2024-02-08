from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from driver import create_chrome_driver
import time
import json
import os


def collect_images(query):
    try:
        search = driver.find_elements("xpath", "//input[@type='text']")[1]
        search.send_keys(query)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        images = driver.find_elements("xpath", "//div[@class='imageResultPreview']")
        print(images)
        driver.back()
    except OSError as err:
        print(err)
        return


desk_path = "/mnt/c/Users/paige/Desktop/microbe_images/"
directories = [entry for entry in os.listdir(desk_path) if os.path.isdir(os.path.join(desk_path, entry))]

driver = create_chrome_driver("https://www.algaebase.org/search/images/")
time.sleep(5)
for query in directories:
    collect_images(query)


