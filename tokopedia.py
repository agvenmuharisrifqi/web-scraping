from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome('chromedriver_linux64/chromedriver')
browser.get('https://www.tokopedia.com')

sleep(2)
browser.find_element(By.CLASS_NAME, 'css-2hev56').click()
