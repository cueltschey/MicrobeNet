import os
from driver import create_chrome_driver
import json
import time


driver = create_chrome_driver("http://galerie.sinicearasy.cz/galerie/akce/2001/specialni-fykologie-2001")

output_path = "/mnt/c/Users/paige/Desktop/sinicearasy"

def collect_images(genus):
    images = [{"name":genus, "image_url":element.get_attribute("src")} for element in driver.find_elements("xpath", "//img")[1:]]
    for image in images:
        print(image["name"], " --> ", image["image_url"])
    with open(os.path.join(output_path, genus + ".json"), "w") as f:
        json.dump(images, f, indent=4)


num_links = len(driver.find_elements("xpath", "//li[contains(@class, 'doc')]"))

for index in num_links:
    try:
        link = driver.find_elements("xpath", "li//[contains(@class, 'doc')]")[index]
        link.click()
        genus = driver.find_elements("xpath", "//h1[@class='page-title']")[0]
        collect_images(genus)

    except: 
        print("Failed")
