from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def create_chrome_driver(url, detach=True):
    options = Options()
    if not detach:
        options.add_experimental_option("detach",False)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    return driver
#scroll_script = "window.scrollTo(0, document.body.scrollHeight);"

#items = driver.find_elements("xpath", "//div[@class='productitem']")
#item.get_attribute("innerHTML")
#driver.execute_script(scroll_script)


