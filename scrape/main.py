import os

# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException


from bs4 import BeautifulSoup as bs

# from splinter import Browser

import time
from datetime import datetime

import json
import re



def countDIV(element):
    i = 0
    for x in element:
        i += 1
    return i

def screenSize():
    driver = _init_browser()
    width = driver.get_window_size().get("width")
    height = driver.get_window_size().get("height")
    screen = [width,height]

    print(width,height)
    return screen


def _init_browser():
  

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--nosandbox")
    chrome_options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)


    
    # options = Options()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.page_load_strategy = 'normal'
    # driver = webdriver.Chrome(**executable_path,options=options)

    return driver



def HPAG(year,topic,mFROM,mTO):
    
    driver = _init_browser()
    HLC_homepage = 'https://www.hapag-lloyd.com/en/home.html' 
    driver.get(HLC_homepage)
    driver.implicitly_wait(10)
    try:
        time.sleep(5)
        privacy = driver.find_element(By.CSS_SELECTOR, ".save-preference-btn-handler")
        privacy.click()
    except NoSuchElementException:
        print('didnt pass cookie check')
        driver.quit()

    driver.maximize_window()
    screenSize()
    driver.implicitly_wait(10)

    try:
        HLC_newspage = f'https://www.hapag-lloyd.com/en/services-information/news.html#selectedtopics={topic}&year={year}&month='
        driver.get(HLC_newspage)

    except:
        driver.quit()
    
    finally:
        print('loop function begins')
        counter = 0
        more = driver.find_element(By.CSS_SELECTOR,'button[class="hal-button hal-button--primary"]')
        while more.is_enabled() is True:
        
            more.click()
            time.sleep(5)
            counter += 1
            wrapper = driver.find_elements(By.XPATH,'/html[1]/body[1]/div[4]/div[2]/div[2]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div')
            if countDIV(wrapper) == 1:
                break
    
    html = driver.page_source
    print(f'LoadMore btn click {counter} times')

    soup = bs(html, 'html.parser')

    articles = soup.find_all('div', class_='hal-teaser-text')
    
    l = []
    for article in articles:
        a = article.find('a', class_='hal-teaser-heading').text
        l.append(a)
        print(a)

    driver.quit()
    return l
    

# HPAG(year,topic)



def _init_SCRAPER(content):
    
    carriers = content['carriers']
    mFROM = content['monthF']
    mTO = content['monthT']
    year = content['year']

    for y in year:
        if len(year) < 2:
            thisY = y
            for c in carriers:
                if c == 'hlc':
                    d1 = HPAG(thisY,'surcharges',mFROM,mTO)
            return d1
        else:
            for c in carriers:
                if c == 'hlc':
                    dA = HPAG(year[0],'surcharges',mFROM,mTO)
                    dB = HPAG(year[0],'surcharges',mFROM,mTO)
            return dA,dB
    # print(carriers,mFROM,mTO,year)




# driver.implicitly_wait(10)
# try:
#     openMenu = driver.find_element(By.CSS_SELECTOR,".hal-navigation-top-menu-icon").click()
#     driver.implicitly_wait(2)
#     clickNews = driver.find_element(By.XPATH,"//span[normalize-space()='Services & Information']").click()
#     driver.implicitly_wait(2)
#     closeMenu = driver.find_element(By.CSS_SELECTOR,".hal-navigation-top-clear-icon").click()
#     print('Browsing by links WORKS!')
# except:
#     print('Loading NewsLink Manually')
#     driver.get('https://www.hapag-lloyd.com/en/services-information/news.html')
# finally:
#     driver.implicitly_wait(3)
#     AllNews = "div[class='hal-newsstream'] a[class='hal-button']"
#     driver.find_element(By.CSS_SELECTOR,AllNews).click()


    


    # driver.implicitly_wait(5)
    # html = driver.page_source

    # print(html)



    # f = Tinput
    # y = Yinput
    # try:

        ##  MAXIMIZE WINDOW TO GET YEAR FILTER  ##
        # driver.maximize_window()
        # # screenSize()
        # yr = driver.find_element(By.XPATH,f'//input[@id="hal-margincolumn-timeline-input-toggle-{y}"]')
        # driver.implicitly_wait(5)
        # yr.click
        # if yr.is_enabled() is True:
        #     yr.click()
        #     print(yr.is_selected())
        # else:
        #     print('yr is not enabled')
        # driver.implicitly_wait(5)
        # filters = {}
        # allfilter = driver.find_element(By.CSS_SELECTOR,'.hal-searchfilter.hal-searchfilter--secondary')
        # filterLabels = allfilter.find_elements(By.TAG_NAME,"label")
        # for x in filterLabels:
        #     checkbox = x.find_element(By.TAG_NAME,"input")
        #     print(checkbox.is_selected())
        #     span = x.find_element(By.TAG_NAME,"span").text
        #     filters.update({span:checkbox})

        # selectFilter = filters[f]
        # selectFilter.click()
        # print(selectFilter.is_selected())
    # except:
    #     print('didnt work!')
    #     driver.quit()


    # loadAllData(Tinput,Yinput)

