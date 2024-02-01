from utils import Downloader, HTMLParser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from driver import create_chrome_driver
import time



downloader = Downloader()
driver = create_chrome_driver("https://www.inaturalist.org/observations?place_id=any&q=microorganism&subview=table")
time.sleep(5)

image_links = driver.find_elements("xpath", "//a[@class='img  ']")
name_links = driver.find_elements("xpath", "//a[@class='display-name sciname' and @href='/observations/*']")

print(len(image_links))
print(len(name_links))

