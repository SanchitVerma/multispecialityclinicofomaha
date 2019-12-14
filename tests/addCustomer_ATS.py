import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class login_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/sanchitverma/PycharmProjects/a4venv/bin/chromedriver')

    def test_blog(self):
        user = "admin"
        pwd = "test12345"
        name = "Sharad Verma"
        insurance = "27816"
        email = "sharadverma@gmail.com"
        phone = "4026713265"
        dob = "10/11/1980"
        address = "16002 Browne Street Omaha"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/clinic-supervisor")
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        time.sleep(2)
        elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[1]/li[2]/a').click()
        time.sleep(2)
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[2]/div/a/span').click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys(name)
        elem = driver.find_element_by_id("id_insurance_number")
        elem.send_keys(insurance)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys(email)
        elem = driver.find_element_by_id("id_phone_number")
        elem.send_keys(phone)
        elem = driver.find_element_by_id("id_dob")
        elem.send_keys(dob)
        elem = driver.find_element_by_id("id_address")
        elem.send_keys(address)
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/form/button').click()
        elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[1]/li[2]/a').click()
        time.sleep(2)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
