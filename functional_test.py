"""
Functional test.

Django TDD - init project
"""
import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    # Initial test to open the browser in the first page

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

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
        self.assertEqual(button.get_attribute('value'), 'Set Time')

        # When user press the button, the page updates, and now the page lists
        # "Start time: "
        table = self.browser.find_element_by_id('id_time_table')
        rows = table.find_elements_by_tag_name('th')
        self.assertTrue(
            any(row.text == 'Start Time' for row in rows)
        )

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
