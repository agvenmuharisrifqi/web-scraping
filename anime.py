from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
from create_excel import CreateExcel

def scrolling_page(browser):
    pass

def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome('chromedriver_linux64/chromedriver', chrome_options=options)

    data = []
    for i in range(1, 11):
        browser.get('https://animasu.club/pencarian/?urutan=abjad&halaman=%s' % (str(i)))
        sleep(2)
        height = 0
        while True:
            sleep(0.5)
            browser.execute_script('window.scrollTo(0, ' + str(height) + ');')
            window_height = browser.execute_script('return document.body.scrollHeight')
            height += 300
            if height > window_height:
                soup = BeautifulSoup(browser.page_source, 'lxml')
                items = soup.find_all('div', attrs={'class': 'bs'})
                item = [
                    (
                        item.find('div', attrs={'class': 'tt'}).text,
                        item.find('div', attrs={'class': 'typez'}).text,
                        item.find('span', attrs={'class': 'sb'}).text
                    ) for item in items
                ]
                data += item
                break
    
    header = ['Judul', 'Type', 'Status']
    excel = CreateExcel(filename='anime.xlsx', header=header)
    excel.add_data(data)
    excel.close()

    sleep(2)
    browser.close()


if __name__ == '__main__':
    main()
