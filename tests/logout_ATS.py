import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Logout(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome()

    def test_logout(self):
        user = "admin"
        pwd = "password!23"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://omaha-fire.herokuapp.com/users/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/nav/div/div/a[3]").click()
        assert "Logged out"
        time.sleep(3)

    def teardown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
