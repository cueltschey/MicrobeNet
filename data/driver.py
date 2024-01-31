from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


#options = Options()
#options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://happygardens.com/collections/wind-spinners-whirligigs?usf_take=56")
products_found = list()

scroll_script = "window.scrollTo(0, document.body.scrollHeight);"

def get_items():
    items = driver.find_elements("xpath", "//div[@class='productitem']")


    for item in items:
        try:
            price_and_name = item.text.split("\n")
            if len(price_and_name) >= 4:
                name = price_and_name[3]
                price = price_and_name[2]
            else:
                name = price_and_name[2]
                price = price_and_name[1]
            html_string = str(item.get_attribute("innerHTML"))
            soup = BeautifulSoup(html_string, "html.parser")
            img_url = "https:" + soup.find_all('img')[0].get('srcset')
            products_found.append((name, price, img_url))
        except:
            print(item.text.split("\n"))

for _ in range(2):
    driver.execute_script(scroll_script)
    time.sleep(3)
    get_items()


