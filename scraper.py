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

class Sel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.aliexpress.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_sel(self):
        driver = self.driver
        delay = 3
        url = "https://www.aliexpress.com/w/wholesale-health-and-fitness-equipment.html?g=y&SearchText=health+and+fitness+equipment"
        for i in range(1, 15):
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

            print(len(divs))

            for div in divs:
                title_div = div.find('div', class_='multi--content--11nFIBL').find('div', class_='multi--title--G7dOCj3').h3
                title = title_div.text.strip() if title_div else "N/A"

                items_sold_span = div.find('div', class_='multi--tradeContainer--3TqP9qf')
                items_sold = items_sold_span.span.text.strip() if items_sold_span and items_sold_span.span else "N/A"

                price_div = div.find('div', class_='multi--price-sale--U-S0jtj')
                price = price_div.text.strip() if price_div else "N/A"

                original_price_span = div.find('div', class_='multi--price-original--1zEQqOK')
                original_price = original_price_span.span.text.strip() if original_price_span and original_price_span.span else "N/A"

                discount_span = div.find('div', class_='multi--discount--3hksz5G')
                discount = discount_span.text.strip() if discount_span else "N/A"

                shipping_info_span = div.find('div', class_='multi--serviceContainer--3vRdzWN')
                shipping_info = shipping_info_span.span.text.strip() if shipping_info_span and shipping_info_span.span else "N/A"

                store_info_span = div.find('span', class_='cards--store--3GyJcot')
                store_info = store_info_span.text.strip() if store_info_span else "N/A"

                print(title, items_sold, price, original_price, discount, shipping_info, store_info)
                print("----------")

            url = f"https://www.aliexpress.com/w/wholesale-health-and-fitness-equipment.html?page={i + 1}&g=y&SearchText=health+and+fitness+equipment"

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
