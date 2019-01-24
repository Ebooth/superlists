from functional_tests.base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_for_one_user(self):
        self.browser.get(self.live_server_url)
        self.assertIn("To-Do", self.browser.title)

        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do", header_text)

        inputbox = self.get_item_input_box()
        self.assertEqual(inputbox.get_attribute(
            'placeholder'), 'Enter a to-do item')
        
        self.add_list_item('Buy peacock feathers')
        self.add_list_item('Use peacock feathers to make a fly')
        
        #check first element is still here
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        

    def test_multiple_users_can_start_lists_at_different_urls(self):

        self.browser.get(self.live_server_url)

       
        self.add_list_item('Buy peacock feathers')

        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        self.browser.quit()
        self.browser = webdriver.Firefox()

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        self.add_list_item('Buy milk')

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

