from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from driver import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import json
import os

driver = create_chrome_driver("https://diatom.ansp.org/algae_image/SearchCriteria.aspx")


results = list()

dropdown = driver.find_element(By.ID, "ContentPlaceHolder1_ddlGenus")
select = Select(dropdown)
select.select_by_value("Achnanthes")
driver.find_element(By.ID, "ContentPlaceHolder1_btnShowThumbnails")

