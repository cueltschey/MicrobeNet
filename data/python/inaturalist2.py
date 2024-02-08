from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from driver import create_chrome_driver
import time
import json
import os




def get_image_urls(driver):
    image_elements = driver.find_elements("xpath", "//a[@class='img  ']")
    urls = [element.get_attribute("style").split("url(")[1][:-2] for element in image_elements]
    return urls

def get_genus_names(driver):
    name_elements = driver.find_elements("xpath", "//a[@class='display-name sciname' or @class='display-name comname' or @class='noname display-name']")
    names = [element.text for element in name_elements if len(element.text)>0]
    return names


def collect_images(query, count):
    print(f"Searching for: {query} #{count}")
    driver = create_chrome_driver(f"https://www.inaturalist.org/observations?place_id=any&subview=table&verifiable=any&q={query}")
    urls = list()
    names = list()
    results = list()
    scroll_chunk_size = 5  
    while True:
        time.sleep(2)  
        for _ in range(scroll_chunk_size):

            new_names = get_genus_names(driver)
            new_image_urls = get_image_urls(driver)
            
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
                print(new_names[i], new_image_urls[i], f"--> {query}.json")


            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            next_page = driver.find_elements("xpath", "//a[contains(@ng-click, 'selectPage')]")[-1]
            next_page_wrapper = driver.find_elements("xpath", "//li[contains(@class, 'pagination')]")[-1]
            print(next_page_wrapper.get_attribute("class"))
            if "disabled" in next_page_wrapper.get_attribute("class"):
                break
            next_page.click()
            print("Next Page")
        except:
            break
    driver.quit()
    with open(f"/mnt/c/Users/paige/Desktop/inaturalist/{query}.json", "w") as f:
        json.dump(results, f, indent=4)



desk_path = "/mnt/c/Users/paige/Desktop/old_microbe_images/"
directories = [entry for entry in os.listdir(desk_path) if os.path.isdir(os.path.join(desk_path, entry))]

count = 0
for query in reversed(directories):
    count += 1
    collect_images(query, count)


