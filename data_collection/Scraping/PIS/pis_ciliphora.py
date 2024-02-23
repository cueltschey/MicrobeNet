## FINISHED


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


driver = create_chrome_driver("http://protist.i.hosei.ac.jp/PDB/Images/Protista/CiliophoraE.html")

time.sleep(2)

links = [link.text for link in driver.find_elements("xpath", "//a[@target='blank']")]
print(links)
driver.quit()

def get_images(link):
    time.sleep(2)
    image_links = driver.find_elements("xpath", "//a[contains(@href, 'html')]")

    results = list()

    for index in range(len(image_links)):
        try:
            image_link = driver.find_elements("xpath", "//a[contains(@href, 'html')]")[index]
        except:
            continue
        image_link.click()
        print("Visiting sublink")
        time.sleep(1)
        images = [image.get_attribute("src") for image in driver.find_elements("xpath", "//img[contains(@src, 'jpg')]")]
        print(images)
        for image in images:
            print(image, f"--> {link}.json")
            results.append({"name": link , "image_url": image})
        driver.back()
    
    with open(os.path.join("..", link + ".json"), "w") as f:
        json.dump(results, f, indent=4)

    driver.back()

for link in links[40:]:
    driver = None
    print("Visiting: ", link)
    driver = create_chrome_driver(f"http://protist.i.hosei.ac.jp/PDB/Images/Ciliophora/{link}/index.html")
    get_images(link)
    driver.quit()


