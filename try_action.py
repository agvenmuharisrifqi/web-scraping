from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


# create webdriver object
driver = webdriver.Chrome('chromedriver_linux64/chromedriver')
 
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
 
# create action chain object
action = ActionChains(driver)
 
# perform the operation
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".consent-btn")))
action.key_down(Keys.CONTROL).send_keys('F').key_up(Keys.CONTROL).perform()