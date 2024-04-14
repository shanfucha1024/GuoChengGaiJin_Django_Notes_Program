from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME,'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):

        #张三听说有一个在线待办事项应用
        #他去看了这个应用的首页
        self.browser.get(self.live_server_url)

        #网页包含'To-Do'这个词
        self.assertIn('To-Do', self.browser.title), "Browser title was " + self.browser.title
        header_text = self.browser.find_element(By.TAG_NAME,'h1').text #(1)
        self.assertIn('To-Do', header_text)

        #应用有一个输入待办事项的文本输入框
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        #在文本输入框中输入了“Buy flowers”
        inputbox.send_keys('Buy flowers') #(2)

        #按回车键后，页面更新了
        #页面中显示了“1: Buy flowers”作为待办事项
        inputbox.send_keys(Keys.ENTER) #(3)
        time.sleep(1) #(4)
        self.check_for_row_in_list_table('1: Buy flowers')

        table = self.browser.find_element(By.ID, 'id_list_table')   
        rows = table.find_elements(By.TAG_NAME, 'tr')   #(1)
        self.assertIn('1: Buy flowers', [row.text for row in rows])
        

        #页面中还有一个文本输入框，可以输入其他待办事项
        #他输入了“Give a gift to Lisi”
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Give a gift to Lisi')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #页面再次更新，显示了两个待办事项
        # table = self.browser.find_element(By.ID, 'id_list_table')
        # rows = table.find_elements(By.TAG_NAME, 'tr')
        # self.assertIn('1: Buy flowers', [row.text for row in rows])
        # self.assertIn('2: Give a gift to Lisi', [row.text for row in rows])
        self.check_for_row_in_list_table('1: Buy flowers')
        self.check_for_row_in_list_table('2: Give a gift to Lisi')

        #他想知道这个网站是否会记住他的待办事项
        #他看到网站为他生成了一个唯一的URL
        self.fail('Finish the test!')

        #他访问这个URL，发现他的待办事项列表还在
        #他很满意，去睡觉了

# if __name__ == '__main__':
#     unittest.main()