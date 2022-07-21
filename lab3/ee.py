# # import random
import re
# # # vowels list
# # vowels = ['a', 'e', 'i', 'o', 'i', 'u']
# #
# # # index of 'e' in vowels
# # index = vowels.index('e')
# # print('The index of e:', index)
# #
# # # element 'i' is searched
# # # index of the first 'i' is returned
# # index = vowels.index('i')
# #
# # print('The index of i:', index)
# #
# #
# #
# # url_list = []
# # new_url_list = []
# # with open("url_list.txt", 'r', encoding='utf-8') as f:
# #     for line in f:
# #         url_list.append('https://www.' + line.replace('\n', ''))
# #
# #
# # print(url_list)
# # random.shuffle(url_list)
# #
# # new_url_list = [el*2 for el in new_url_list]
# #
# # print(new_url_list)
#
#
# from selenium import webdriver
#
# class GoogleOrgSearch():
#
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#
#     def test_google_search_page(self):
#         driver = self.driver
#         driver.get("http://www.cdot.in")
#         window_before = driver.window_handles[0]
#         print(window_before)
#         driver.find_element_by_xpath("//a[@href='http://www.cdot.in/home.htm']").click()
#         window_after = driver.window_handles[1]
#         driver.switch_to.window(window_after)
#         print(window_after)
#         driver.find_element_by_link_text("ATM").click()
#         driver.switch_to.window(window_before)
#
#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == "__main__":
#     main()

# m = re.search('(?<=abc)def', 'abcdef')
# m.group(0)
# print(m)
#
# nn = re.search('(еатральн)[а-я .,]+[1]?', 'Театральная, дом блят 1')
# nn.group(0)
# print(nn)

for p in range(2):
    print(p)

# if 'альная пл., 1' in r'(еатральн)[а-я .,]+[1]+':
#     print('True')
# else:
#     print('false')