import os
import time
import json
from driver import create_chrome_driver


def get_links():
    driver = create_chrome_driver("https://microfloraenfauna.com/")
    
    time.sleep(2)
    links = driver.find_elements("xpath", "//li//a[contains(@href, 'micro')]")
    urls = [link.get_attribute("href") for link in links][1:-8]

    return urls

def get_images(url):
    driver = create_chrome_driver(url)
    time.sleep(2)
    images = None



urls = get_links()


for url in urls:
    print("Visiting: ", url)
