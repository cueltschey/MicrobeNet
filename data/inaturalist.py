from utils import Downloader, HTMLParser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from driver import create_chrome_driver
import time
import json



downloader = Downloader()
driver = create_chrome_driver("https://www.inaturalist.org/observations?place_id=any&q=microorganism&subview=table")

def get_image_urls():
    image_elements = driver.find_elements("xpath", "//a[@class='img  ']")
    urls = [element.get_attribute("style").split("url(")[1][:-2] for element in image_elements]
    return urls

def get_genus_names():
    name_elements = driver.find_elements("xpath", "//a[@class='display-name sciname' or @class='display-name comname' or @class='noname display-name']")
    names = [element.text for element in name_elements if len(element.text)>0]
    return names

results = list()
urls = list()
names = list()

scroll_chunk_size = 4  
for _ in range(scroll_chunk_size):
    time.sleep(2)  

    new_names = get_genus_names()
    new_image_urls = get_image_urls()
    
    for i in range(len(new_names)):
        if i >= len(new_image_urls):
            break
        if new_image_urls[i] in urls or len(new_names[i]) == 0:
            continue
        item = dict()
        item["image_url"] = new_image_urls[i]
        item["name"] = new_names[i]
        results.append(item)
        urls.append(new_image_urls[i])
        names.append(new_names[i])


    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


with open("inaturalist.json", "w") as f:
    json.dump(results, f, indent=4)


driver.quit()

desk_path = "C:\\Users\\paige\\Desktop\\microbe_images"
count = 0
for item in results:
    count += 1
    genus = ""
    if item["name"].split(" ")[0] == "Genus":
        genus = item["name"].split(" ")[1]
    else:
        genus = item["name"].split(" ")[0]

    Downloader.download_image(item["image_url"], desk_path, f"{genus}\\inaturalist_{count}")


