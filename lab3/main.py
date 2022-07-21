import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import random


class Test(unittest.TestCase):

    @property
    def test_func(self):
        service = Service("E:\\_ucheba+rabota\\Ucheba\\8sem\\srv\\lab1\\firefox_driver\\geckodriver.exe")
        driver = webdriver.Firefox(service=service)
        my_address = '(еатральн)[а-я .,]+[1]?'
        rel_counter = 0
        links_number = 0
        driver.set_page_load_timeout(12)
        url = 'https://google.com'

        try:
            driver.set_window_size(1920, 570)
            driver.get(url=url)

            search_field = driver.find_element(By.NAME, 'q')
            search_field.send_keys('Большой театр')
            time.sleep(2)

            search_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')


            search_button.click()

            def parse_links(my_address, rel_counter, old_links_number):
                result_list_names = []
                result_list = driver.find_elements(By.PARTIAL_LINK_TEXT, 'https')

                print(result_list)
                for item in result_list:
                    result_list_names.append(item.text[:item.text.find("\n")])
                    a = item.get_attribute('href')
                    index = result_list.index(item)
                    print(f'{index + 1} trying {a} ...')

                    driver.switch_to.new_window('tab')
                    try:
                        driver.get(url=a)
                        time.sleep(5)
                        t = driver.find_element(by=By.TAG_NAME, value='body').text.lower()
                        if re.search(my_address, t):
                            rel_counter += 1
                            print('...succ')
                        else:
                            print('...FAIL')
                    except Exception as ex1:
                        print(ex1)

                    time.sleep(4)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                return rel_counter, old_links_number + len(result_list)


            time.sleep(3)

            for p in range(2):
                #p = 1
                print(f'prep page {p+1}')
                if p == 1:
                    a = driver.find_elements(by=By.ID, value='pnnext')
                    for elem in a:
                        if elem.text == 'Следующая':
                            time.sleep(4)
                            elem.click()
                            time.sleep(4)
                rel_counter, links_number = parse_links(my_address, rel_counter, links_number)

            print(f'{rel_counter} из {links_number} ссылок релевантны.')

            print('Shutting down in 5 seconds...')
            time.sleep(5)


        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()


RExemp = Test()
RExemp.test_func
