from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from driver import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import json
import os

driver = create_chrome_driver("https://diatom.ansp.org/algae_image/SearchCriteria.aspx")



dropdown = driver.find_element(By.ID, "ContentPlaceHolder1_ddlGenus")
select = Select(dropdown)
options = [option.text for option in select.options]


def download_images(option):
    print(option)
    results = list()
    try:
        current = driver.find_element("xpath", f"//option[@value='{option}']")
        current.click()
    except:
        return
    driver.find_element(By.ID, "ContentPlaceHolder1_btnShowThumbnails").click()
    images =  [element.get_attribute("src") for element in driver.find_elements("xpath", "//img[contains(@src, 'diatom')]")]

    driver.back()

    for image in images:
        print(image)
        results.append({"name":"option", "image_url": image})
    with open(os.path.join("..", f"{option}.json"), "w") as f:
        json.dump(results, f, indent=4)


for option in options[3:]:
    download_images(option)
