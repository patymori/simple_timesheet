"""
Functional test.

Django TDD - init project
"""
import unittest
from datetime import datetime

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    # Initial test to open the browser in the first page

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def check_for_column_in_list_table(self, header_text, time_punch):
        table = self.browser.find_element_by_id('id_time_table')
        table_head = table.find_elements_by_tag_name('th')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(header_text, [thead.text for thead in table_head])
        self.assertIn(time_punch, [row.text for row in rows])

    def test_must_open_home_page(self):
        # User access the website
        self.browser.get('http://localhost:8000')

        # User sees the page title and header says 'Simple Time Sheet'
        self.assertIn('Simple Time Sheet', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Simple Time Sheet', header_text)

        # User can press a button to set the starting time in the time sheet
        button = self.browser.find_element_by_tag_name('button')
        self.assertEqual(button.get_attribute('type'), 'submit')
        self.assertEqual(button.text, 'Punch In')

        # When user press the button, the page updates, and now the page lists
        # "Start time: <time>"
        start_time = datetime.strftime('%H:%M')
        button.click()
        time.sleep(1)
        self.check_for_column_in_list_table('Start Time', start_time)

        # User can press a button to set the ending time in the time sheet
        button = self.browser.find_element_by_tag_name('button')
        self.assertEqual(button.get_attribute('type'), 'submit')
        self.assertEqual(button.text, 'Punch Out')

        # When user press the button again, the page updates, and now the page
        # lists "End time: <time>"
        end_time = datetime.strftime('%H:%M')
        button.click()
        time.sleep(1)

        self.check_for_column_in_list_table('Start Time', start_time)
        self.check_for_column_in_list_table('End Time', end_time)

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
