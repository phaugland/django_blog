import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LMS_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_role_assign(self):
        user = "testadmin"
        pwd = "Q5jYjhypRtkX79uw"
        title = " with new text"
        text = " Now with automated test text."
        driver = self.driver
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h2/a").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/a").click()
        time.sleep(3)
        elem = driver.find_element_by_id("id_title")
        elem.send_keys(title)
        time.sleep(3)
        elem = driver.find_element_by_id("id_text")
        elem.send_keys(text)
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        time.sleep(5)
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

