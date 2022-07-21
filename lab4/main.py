import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time


class Test(unittest.TestCase):

    @property
    def test_func(self):
        service = Service("E:\\_ucheba+rabota\\Ucheba\\8sem\\srv\\lab1\\firefox_driver\\geckodriver.exe")
        driver = webdriver.Firefox(service=service)
        articles_names = []
        articles_links = []
        articles_previews = []
        articles_ids = []

        driver.set_page_load_timeout(12)
        url = 'https://habr.com/ru/company/lamptest/blog/'

        try:
            driver.set_window_size(1920, 630)
            driver.get(url=url)

            time.sleep(2)
            pain_counter = 0
            articles_list = driver.find_elements(by=By.TAG_NAME, value='article')
            for article in articles_list:
                max_arts = 5
                if pain_counter < max_arts:
                    time.sleep(3)
                    print(f'\nscrolled to article_name ({pain_counter + 1} out of {max_arts})')
                    driver.execute_script("arguments[0].scrollIntoView();", article)
                    driver.execute_script("""window.scrollBy({
                                            top: -50,
                                            left: 0,
                                            behavior: 'smooth'
                                            })""")
                    time.sleep(3)

                    art_id = article.id
                    articles_ids.append(art_id)
                    a = article.find_element(by=By.CLASS_NAME, value='tm-article-snippet__title-link')
                    name = a.text
                    articles_names.append(name)
                    link = a.get_attribute('href')
                    articles_links.append(link)
                    preview = article.find_element(by=By.CLASS_NAME, value='article-formatted-body').text
                    articles_previews.append(preview)
                    time.sleep(3)

                    print(f'Название статьи: {name}')
                    print(f'Превью: {preview}')
                    print(f'Перехожу по ссылке: {link} ...')

                    driver.switch_to.new_window('tab')
                    try:
                        driver.get(url=link)
                        time.sleep(5)
    #     ##      ##     ## Драйвер на новой вкладке!
                        art_text = driver.find_element(by=By.TAG_NAME, value='article').find_element(by=By.CLASS_NAME, value='article-formatted-body').text
                        #print(f' ##################################### \nПолный текст статьи: {art_text}')

                        print("пошло жесткое анализирование текста")
                        preview_by_words = preview.replace('.', '').split(' ')
                        text_by_words = art_text.replace('.', '').split(' ')
                        words_dict = dict.fromkeys(preview_by_words, 0)
                        for word in text_by_words:
                            if word in preview_by_words:
                                words_dict[word] += 1
                        sorted_words_dict = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
                        print(f'СЛОВАРЬ {sorted_words_dict}')

                        dead_end = driver.find_element(by=By.CLASS_NAME, value='tm-article-blocks__comments')
                        driver.execute_script("arguments[0].scrollIntoView();", dead_end)
                        print('scrolled to DEAD_END')
                        driver.execute_script("""window.scrollBy({
                            top: -55,
                            left: 0,
                            behavior: 'smooth'
                            })""")
                        time.sleep(3)

                    except Exception as ex1:
                        print(ex1)
                    finally:
                        time.sleep(4)
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        pain_counter += 1

            time.sleep(3)
            print('Shutting down in 5 seconds...')
            time.sleep(5)


        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()


RExemp = Test()
RExemp.test_func
