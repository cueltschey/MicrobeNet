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
    results = list()
    print("Visisting: ", query)
    try:
        search = driver.find_elements("xpath", "//input[@type='text']")[2]
    except OSError as err:
        print(err)
        return
    search.send_keys(query)
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    images = [element.get_attribute("style").split("url(")[-1].split(");")[0] for element in driver.find_elements("xpath", "//div[contains(@class, 'image')]")]
    print(images)
    results += [image for image in images if image not in results]
    if len(results) > 0:
        with open(os.path.join("/mnt/c/Users/paige/Desktop/algaebase", query + ".json"), "w") as f:
            json.dump(results, f, indent=4)
    driver.back()


desk_path = "/mnt/c/Users/paige/Desktop/old_microbe_images/"
directories = [entry for entry in os.listdir(desk_path) if os.path.isdir(os.path.join(desk_path, entry))]

driver = create_chrome_driver("https://www.algaebase.org/search/images/")
time.sleep(5)
for query in directories:
    try:
        collect_images(query)
    except:
        print("error")
