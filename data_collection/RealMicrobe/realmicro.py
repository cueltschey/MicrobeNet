from driver import create_chrome_driver
import time
import json

primary_url = "https://realmicrolife.com/all-procaryonts/"


def get_page_links(url):
    driver = create_chrome_driver(url)
    page_links = list()
    genus_names = list()
    scroll_chunks = 10
    time.sleep(5)
    for _ in range(scroll_chunks):
        time.sleep(1)
        new_links = driver.find_elements("xpath", "//a[@class='pgcsimplygalleryblock-justified-item-button']")
        page_links += [link for link in new_links if link not in page_links]
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.quit()
    return page_links

def get_images(url):
    driver = create_chrome_driver(url)
    results = list()
    for item in driver.find_elements("xpath", "//img[contains(@class, 'size-full')]"):
        new_entry = dict()
        new_entry["name"] = item.get_attribute("alt").split("-")[0]
        new_entry["image_url"] = item.get_attribute("src")
        print(new_entry)
    driver.quit()
    return results


links = get_page_links(primary_url)

count = 0
for link in links:
    print(link)
    print(link.get_attribute("href"))
    #results = get_images(link.get_attribute("href"))
    results = list()
    with open(os.path.join("/mnt/c/Users/paige/Desktop/realmicrolife", f"real_{count}.json"), "w") as f:
        json.dump(results, f, indent=4)


