from django.test import LiveServerTestCase
from selenium import webdriver

class MyTest(LiveServerTestCase):

    def test_stuff(self):
        browser = webdriver.Firefox()
        self.addCleanup(browser.quit)
        browser.get(self.live_server_url)
        header = browser.find_element_by_tag_name('h1')
        self.assertIn('Hello', header.text)
        browser.find_element_by_link_text('link to home').click()
        header = browser.find_element_by_tag_name('h1')
        self.assertIn('Hello', header.text)        
        self.assertEqual(header.value_of_css_property('color'), 'rgba(255, 0, 0, 1)')


