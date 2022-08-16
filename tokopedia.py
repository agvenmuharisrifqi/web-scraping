from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--no-sandbox')
# options.add_argument('--headless')
options.add_experimental_option("excludeSwitches", ["enable-automation"])


browser = webdriver.Chrome('chromedriver_linux64/chromedriver', chrome_options=options)

browser.get('https://www.tokopedia.com/')

sleep(2)
search_bar = browser.find_element(By.CLASS_NAME, 'e110g5pc0')
search_bar.send_keys('wifi repeater' + Keys.ENTER)

# Scroll Page
i = 350
soup = []
while True:
    sleep(0.25)
    browser.execute_script("window.scrollTo(0, " + str(i) + ");")
    new_height = browser.execute_script("return document.body.scrollHeight")
    i += 350
    if (i > new_height):
        soup = BeautifulSoup(browser.page_source, 'lxml')
        break


# Create File From Scrapped Data
file = open('tokopedia.html', 'w')
file.write(soup.prettify())

browser.close()