from driver import create_chrome_driver
import os
import json
import time

driver = create_chrome_driver("http://plankton.image.coocan.jp/algae1-1-1.html")

output_path = "/mnt/c/Users/paige/Desktop/coocan"

def collect_images(genus):
    time.sleep(5)
    images = list()
    results = list()

    for _ in range(5):
        for image in driver.find_elements("xpath", "//a[contains(@onclick, 'Hpb')]"):
            if image.get_attribute("onclick") not in images:
                images.append(image.get_attribute("onclick"))

        for image in images:
            item = dict()
            item["name"] = genus
            item["image_url"] = image.split("(")[1].split(")")[0][1:-1]
            print(item["name"], " --> ", item["image_url"])
            results.append(item)

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    with open(os.path.join(output_path, genus + ".json"), "w") as f:
        print("Writing: ", len(results), "items to file", genus + ".json")
        json.dump(results, f, indent=4)




time.sleep(5)
for index in range(len(driver.find_elements("xpath", "//a[i]"))):
    time.sleep(5)
    link = driver.find_elements("xpath", "//a[i]")[index]
    if "（" in link.text:
        genus = link.text.split("（")[1][:-1]
    elif "(" in link.text:
        genus = link.text.split("(")[1][:-1]
    else:
        continue
    link.click()
    collect_images(genus)

