from driver import create_chrome_driver
import time




def get_page_links(url):
    driver = create_chrome_driver(url)
    page_links = list()
    genus_names = list()
    scroll_chunks = 10
    for _ in range(scroll_chunks):
        time.sleep(2)
        new_links = driver.find_elements("xpath", "//a[@class='pgcsimplygalleryblock-justified-item-button']")
        for link in new_links:
            if link in page_links:
                continue
            genus_names.append(link.text)
            page_links.append(link)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print(genus_names)
    print(len(page_links))
    print(len(genus_names))
    return genus_names, page_links


genus_names, links = get_page_links("https://realmicrolife.com/all-procaryonts/")
genus_names_2, links_2 = get_page_links("https://realmicrolife.com/all-procaryonts/")
genus_names_3, links_3 = get_page_links("https://realmicrolife.com/all-procaryonts/")

final_genus = list()

for index in range(len(genus_names)):
    if genus_names[index] == '':
        if genus_names_2[index] == '':
            final_genus.append(genus_names_3[index])
        else:
            final_genus.append(genus_names_2[index])
    else:
        final_genus.append(genus_names[index])
print(final_genus)





