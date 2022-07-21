import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
import random


class Test(unittest.TestCase):

    def test_func(self):

        url_list = []
        service = Service("E:\\_ucheba+rabota\\Ucheba\\8sem\\srv\\lab1\\firefox_driver\\geckodriver.exe")
        driver = webdriver.Firefox(service=service)

        url = 'https://yandex.ru'
        linksshort = []

        # link_list = driver.find_elements(by=By.TAG_NAME, value='a')
        # for link in link_list:
        #     linksshort.append(link_list[link[:3]])
        # print(linksshort)



        #
        #
        # new_url_list = [el.replace('https://www.', '') for el in url_list]
        # print(new_url_list)

        try:
            driver.set_window_size(1920, 700)
            driver.get(url=url)
            # if url != url_list[-1]:
            # driver.switch_to.new_window('tab')

            # else:
            time.sleep(1)
            link_list = driver.find_elements(by=By.TAG_NAME, value='a')
            while len(linksshort) < 30:
                for link in link_list:
                    linksshort.append(link.get_attribute('href')) # исходный порядок ссылок
            print(linksshort)

            link_list_sorted = sorted(linksshort) # отсортированный список ссылок
            for elem in link_list_sorted:
                print(elem[:40])

            for link_2 in link_list_sorted:
                driver.switch_to.new_window('tab')
                driver.get(url=link_2)
                time.sleep(1)

            for element in linksshort:
                link_list_sorted.index(element)
                # print(

            driver.switch_to.window(driver.window_handles[j - b])
            #         # Получение имени сайта
            #         titlename = driver.title
            driver.title()



            # print(linksshort[:20])
            # for element in li
            # print(type(linksshort[0]))

            # for win in url_list.__reversed__():
            #     index = url_list.index(win)
            #     print(index+1, win, 'was closed')
            #
            #     driver.switch_to.window(driver.window_handles[index])
            #     driver.close()

            time.sleep(1)

            time.sleep(3)


        except Exception as ex:
            print(ex)
        finally:
            #driver.close()
            driver.quit()


RExemp = Test()
RExemp.test_func()
