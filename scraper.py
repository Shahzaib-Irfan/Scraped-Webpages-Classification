import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys
import unittest
import time
import re
import csv

class Sel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_sel(self):
        driver = self.driver
        delay = 3
        url = "https://www.aliexpress.com/w/wholesale-Food.html?g=y&SearchText=Food"
        for i in range(1, 16):
            print(f"Page: {i}")
            driver.get(url)

            start = 0
            end = driver.execute_script("return document.body.scrollHeight") / 4
            for _ in range(1, 3):
                driver.execute_script(f"window.scrollTo({start}, {end});")
                start = end
                end += end
                time.sleep(4)
            html_source = driver.page_source
            soup = BeautifulSoup(html_source, 'html.parser')
            divs = soup.find_all('div', class_='list--gallery--C2f2tvm search-item-card-wrapper-gallery')

            titles = []
            for div in divs:
                title_div = div.find('div', class_='multi--content--11nFIBL').find('div', class_='multi--title--G7dOCj3').h3
                title = title_div.text.strip() if title_div else "N/A"
                titles.append(title)
                print(title)
                print("----------")

            url = f"https://www.aliexpress.com/w/wholesale-Food.html?page={i + 1}&g=y&SearchText=Food"
            complete_title = " ".join(titles)
            
            with open('Webpages.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([complete_title, "Food"])

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
