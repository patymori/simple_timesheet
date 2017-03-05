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
        self.browser.get('http://localhost:8000')
        self.assertIn('Simple Time Sheet', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
