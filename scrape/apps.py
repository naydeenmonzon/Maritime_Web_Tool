import os
from django.apps import AppConfig
from selenium import webdriver

class ScrapeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scrape'


GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
chrome_bin = os.environ.get('GOOGLE_CHROME_BIN', 'chromedriver')
options = webdriver.ChromeOptions()
options.binary_location = chrome_bin
options.add_argument('-- disable-gpu')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = GOOGLE_CHROME_PATH


browser = webdriver.Chrome(execution_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)