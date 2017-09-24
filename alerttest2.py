from selenium import webdriver
import unittest
import time

class CompareProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('http://demo-store.seleniumacademy.com/')

    def test_compare_products_removal_alert(self):
        # get the search textbox
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()

        # enter search keyword and submit
        search_field.send_keys('phones')
        search_field.submit()
        time.sleep(2)

        # click the Add to compare link
        self.driver.\
            find_element_by_link_text('Add to Compare').click()
        time.sleep(2)

        # click on Remove this item link,
        # this will display an alert to the user
        self.driver.find_element_by_link_text('Clear All').click()
        time.sleep(2)

        # switch to the alert
        alert = self.driver.switch_to.alert
        time.sleep(2)

        # get the text from alert
        alert_text = alert.text
        time.sleep(2)

        # check alert text
        self.assertEqual('Are you sure you would like to remove all products from your comparison?',
                          alert_text)
        time.sleep(2)

        # click on Ok button
        alert.accept()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)