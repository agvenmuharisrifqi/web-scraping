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
search_bar.send_keys('xiaomi poco 3' + Keys.ENTER)

# Scroll Page
wait = WebDriverWait(browser, 3)
soup = []
for i in range(10):
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'css-12sieg3')))
    height = 0
    soup = []
    while True:
        sleep(0.5)
        browser.execute_script("window.scrollTo(0, " + str(height) + ");")
        window_height = browser.execute_script("return document.body.scrollHeight")
        height += 350
        if (height > window_height):
            sleep(2)
            wait.until(EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Laman berikutnya"][@class="css-1eamy6l-unf-pagination-item"]')))
            next = browser.find_element(By.XPATH, '//button[@aria-label="Laman berikutnya"][@class="css-1eamy6l-unf-pagination-item"]')
            next.click()
            soup = BeautifulSoup(browser.page_source, 'lxml')
            # file = open('tokopedia.html', 'w')
            # file.write(soup.prettify())
            break

# Create File From Scrapped Data

# browser.close()