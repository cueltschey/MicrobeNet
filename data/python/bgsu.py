from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from driver import create_chrome_driver
import time
import json
import os



driver = create_chrome_driver("https://www.bgsu.edu/arts-and-sciences/biological-sciences/facilities-and-resources/algal-microscopy-laboratory/image-archive.html")
time.sleep(5)
links = driver.find_elements("xpath", "//a[contains(@href, 'image-archive')]")
print(links)


count = 0
for link in links:
    couunt += 1
    link.click()
    images = driver.find_elements("xpath", "//a[contains(@href, 'image')]")
    results = list()
    for image in images:
        print(image)
        try:
            results.append({"name":image.text, "image_url": image.get_attribute("href")})
        except:
            print("fail")
    with open(os.path.join("..", f"pis_{count}" + ".json"), "w") as f:
        json.dump(results, f, indent=4)
    driver.back()
