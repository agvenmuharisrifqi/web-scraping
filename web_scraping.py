from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from time import sleep

browser = webdriver.Chrome('chromedriver_linux64/chromedriver')
  
browser.get('http://localhost:8090/')

username = browser.find_element(By.ID, 'login').send_keys('admin@artsys.id')
password = browser.find_element(By.ID, 'password').send_keys('12345' + Keys.ENTER)

sleep(2)
browser.find_element(By.CSS_SELECTOR, '.dropdown-toggle').click()
browser.find_element(By.LINK_TEXT, 'Odoo Rest API').click()
# browser.quit()
