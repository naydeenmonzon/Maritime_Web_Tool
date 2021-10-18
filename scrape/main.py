from selenium import webdriver
import os
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service

s = Service('C:\\bin\\chromedriver.exe')
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--nosandbox")
driver = webdriver.Chrome(service =s, options=chrome_options)


