import os
from driver import create_chrome_driver
import json
import time



output_path = "/mnt/c/Users/paige/Desktop/sinicearasy"

def collect_images(url):
    internal_driver = create_chrome_driver(url)
    time.sleep(5)
    genus = internal_driver.find_element("xpath", "//h1[@class='pageTitle']").text
    images = [{"name":genus, "image_url":"http://galerie.sinicearasy.cz/" + element.get_attribute("data-src")} for element in internal_driver.find_elements("xpath", "//img[contains(@data-src, '/')]")]
    internal_driver.quit()
    print(genus, ":\n")
    if len(images) == 0:
        return
    for image in images:
        print(image["name"], " --> ", image["image_url"])
    if os.path.exists(os.path.join(output_path, genus+ ".json")):
        previous_images = list()
        with open(os.path.join(output_path, genus + ".json"), "r") as f:
            print("Reading in: ", genus + ".json")
            previous_images = json.load(f)
        images += previous_images

    with open(os.path.join(output_path, genus + ".json"), "w") as f:
        print("Writing...")
        json.dump(images, f, indent=4)

def get_urls():
    driver = create_chrome_driver("http://galerie.sinicearasy.cz/galerie/")
    time.sleep(5)
    urls = [element.get_attribute("href") for element in driver.find_elements("xpath", "//a[contains(@class, 'node_id')]")]
    driver.quit()
    return urls

urls = get_urls()
print(f"Found {len(urls)} links")

for url in urls:
    try:
        if "akce" in url:
            print("skip ", url)
            continue
        print("Visiting: ", url)
        collect_images(url)

    except Exception as e: 
        print(e)
