import os
import json
import time
from driver import create_chrome_driver



def get_info():
    driver = create_chrome_driver("https://planktonnet.awi.de/index.php?contenttype=image_details&itemid=62207#content")
    time.sleep(3)
    name = driver.find_elements("xpath", "//span[@class='taxontitle']")[0].text
    image_url = driver.find_elements("xpath", "//img")[-8].get_attribute("src")
    return name, image_url

print(get_info())
