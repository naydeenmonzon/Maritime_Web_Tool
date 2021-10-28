from django.test import TestCase

# Create your tests here.
import os
from re import fullmatch
from bs4.element import Tag, SoupStrainer
from splinter import Browser
from bs4 import BeautifulSoup
import requests
from splinter.driver.webdriver import find_by
from webdriver_manager.chrome import ChromeDriverManager
from dataclasses import dataclass
import time


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

def scrapeHLC():
    
    br = init_browser()
    url = "https://www.hapag-lloyd.com/en/services-information/news.html"

    br.visit(url)
