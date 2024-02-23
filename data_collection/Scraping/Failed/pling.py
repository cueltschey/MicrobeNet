import os
import json
import time
from driver import create_chrome_driver

def get_urls(url):
    driver = create_chrome_driver(url)
    time.sleep(2)

    return [link.get_attribute("href") for link in driver.find_elements("xpath", "//td//a[font]")]

print(get_urls("https://www.plingfactory.de/Science/Atlas/Kennkarten%20Procaryota/e-procaryota/01_e-procaryo.html"))
