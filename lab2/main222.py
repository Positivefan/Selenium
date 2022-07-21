import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
import random


class Test():

    def test_func(self):
        service = Service("E:\\_ucheba+rabota\\Ucheba\\8sem\\srv\\lab1\\firefox_driver\\geckodriver.exe")
        driver = webdriver.Firefox(service=service)

        linksshort = []




        try:
            url = 'jut.su'
            driver.set_window_size(1920, 700)
            driver.get(url=url)
            time.sleep(4)

            link_list = driver.find_elements(by=By.TAG_NAME, value='a')
            for link in link_list:
                linksshort.append(link_list[link[:3]])
            print(linksshort)

            # element = driver.find_element(by=By.CLASS_NAME, value='calcsoft')

            #aaa = driver.find_element(by=By.)

#             driver.execute_script("arguments[0].scrollIntoView();", element)
#
#             my_buttons_names = []
#             my_buttons = driver.find_elements(by=By.TAG_NAME, value='button')
#             for button in my_buttons:
#                 my_buttons_names.append(button.text)
#
#             print('my buttons found successfully!')
#             print(my_buttons_names)
#
#
#             dict_buttons = dict(zip(my_buttons_names, my_buttons))
#             #print(dict_buttons)
#
# #           perform    ////////////////////////////////////////////////////////////
# #
# #           Складываем два числа //////////////////////////////
#             print('Складываем два числа... 15 + 37 =', 15 + 37)
#             time.sleep(5)
#
#             dict_buttons['2'].click()
#             dict_buttons['5'].click()
#             time.sleep(2)
#             dict_buttons['+'].click()  # Операция
#             time.sleep(2)
#             dict_buttons['3'].click()
#             dict_buttons['7'].click()
#             time.sleep(2)
#             dict_buttons['='].click()
#
#
#             time.sleep(10)
#             dict_buttons['AC'].click()
#             print("успех")
#
# #           Перемножаем два числа //////////////////////////////
#             print('Перемножаем два числа... 21 * 5 =', 21 * 5)
#             time.sleep(5)
#
#             dict_buttons['2'].click()
#             dict_buttons['1'].click()
#             time.sleep(2)
#             dict_buttons['X'].click()  # Операция
#             time.sleep(2)
#             dict_buttons['5'].click()
#             #dict_buttons['7'].click()
#             time.sleep(2)
#             dict_buttons['='].click()
#
#             time.sleep(10)
#             dict_buttons['AC'].click()
#             print("успех")
#
# #           Возв числа 1 в степень числа 2 //////////////////////////////
#             print('Возводим в степень... 21^9 =', 21**9)
#             time.sleep(5)
#
#             dict_buttons['2'].click()
#             dict_buttons['1'].click()
#             time.sleep(2)
#             dict_buttons['XY'].click()  # Операция
#             time.sleep(2)
#             dict_buttons['9'].click()
#             #dict_buttons['0'].click()
#             time.sleep(2)
#             dict_buttons['='].click()
#
#             time.sleep(10)
#             dict_buttons['AC'].click()
#             print("успех")
#
# #           Чек памяти mSave, mRead, mClear //////////////////////////////
#             print('Тестим память... 510, MS, C, 78, MR, MC')
#             time.sleep(5)
#
#             dict_buttons['5'].click()
#             dict_buttons['1'].click()
#             dict_buttons['0'].click()
#             time.sleep(2)
#             dict_buttons['MS'].click()  # Операция
#             time.sleep(5)
#
#             dict_buttons['C'].click()  # Очист экрана
#             time.sleep(4)
#             dict_buttons['7'].click()
#             dict_buttons['8'].click()
#             time.sleep(5)
#             dict_buttons['MR'].click()  # Вывод из памяти
#             time.sleep(5)
#
#             dict_buttons['MC'].click()
#
#             time.sleep(10)
#             dict_buttons['AC'].click()
#             print("успех")
#             time.sleep(5)


        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()


RExemp = Test()
RExemp.test_func()
