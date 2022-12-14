from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from manipulate_json import update_json_file, get_keys_json
from time import sleep

def scroll_page(browser):
    height = 0
    while True:
        sleep(0.5)
        browser.execute_script('window.scrollTo(0, ' + str(height) + ');')
        window_height = browser.execute_script('return document.body.scrollHeight')
        height += 300
        if height > window_height:
            sleep(1)
            return browser.page_source
        
def get_my_last_page():
    i = 1
    for page in get_keys_json('anime.json'):
            if page == 'page' + str(i):
                i += 1
    return i


def main():

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=750,500')
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome('chromedriver_linux64/chromedriver', chrome_options=options)
    browser.set_window_position(0, 300)

    action = ActionChains(browser)

    key_keyword = 'page'
    i = get_my_last_page()
    browser.get('https://animasu.club/pencarian/?urutan=abjad&halaman=%s' % (str(i)))
    original_window = browser.current_window_handle
    while True:
        sleep(1)
        height = 0
        while True:
            sleep(0.25)
            browser.execute_script('window.scrollTo(0, ' + str(height) + ');')
            window_height = browser.execute_script('return document.body.scrollHeight')
            height += 300
            if height > window_height:
                items = browser.find_elements(By.CLASS_NAME, 'bs')
                for item in items:
                    link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
                    browser.execute_script('window.open("%s", "_blank")' % (link))
                break
        
        data = {}
        for window_handle in browser.window_handles:
            if window_handle != original_window:
                browser.switch_to.window(window_handle)
                sleep(2)
                page_source = scroll_page(browser)
                wait = WebDriverWait(browser, 30)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[itemprop="headline"]')))
                soup = BeautifulSoup(page_source, 'lxml')
                title = soup.find('h1', attrs={'itemprop': 'headline'}).text
                episode = 0
                try:
                    episode = len(soup.find('ul', attrs={'id': 'daftarepisode'}).find_all('li'))
                except:
                    episode = 'comming soon'
                link = browser.current_url
                description_wrapper = soup.find('div', attrs={'class': 'spe'})
                descriptions = {
                    description.text.split(':')[0] if len(description.text.split(':')) > 1 else 'other'
                    :
                    description.text.split(':')[1] if len(description.text.split(':')) > 1 else description.text.split(':')[0]
                    for description in description_wrapper.find_all('span')
                }
                descriptions['Episode'] = episode
                descriptions['Link'] = link

                data[title] = descriptions
                
                browser.close()
                browser.switch_to.window(original_window)
        update_json_file('anime.json', key_keyword + str(i), data)
        if not browser.find_element(By.CSS_SELECTOR, 'a.r').is_displayed():
            break
        else:
            sleep(3)
            print(i)
            i += 1
            browser.get('https://animasu.club/pencarian/?urutan=abjad&halaman=%s' % (str(i)))

    sleep(2)
    browser.close()
    browser.quit()


if __name__ == '__main__':
    main()
