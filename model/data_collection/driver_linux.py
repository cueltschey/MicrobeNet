from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def create_driver(url, browser="firefox"):
    """
    Function to create a Selenium WebDriver instance.
    
    Parameters:
        browser (str): The browser for which WebDriver needs to be created. Options: 'chrome' or 'firefox'.
    
    Returns:
        WebDriver: Selenium WebDriver instance.
    """
    if browser.lower() == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
        raise ValueError("Unsupported browser. Please choose 'chrome' or 'firefox'.")
    driver.get(url)    
    return driver
