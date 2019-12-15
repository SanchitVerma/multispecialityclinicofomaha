import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from multispecialityclinicofomaha.tests import login_ATS, logout_ATS, editProvider_ATS
from multispecialityclinicofomaha.tests import addCustomer_ATS, deleteAppointment_ATS

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTest(loader.loadTestsFromModule(login_ATS))
suite.addTest(loader.loadTestsFromModule(logout_ATS))
suite.addTest(loader.loadTestsFromModule(editProvider_ATS))
suite.addTest(loader.loadTestsFromModule(addCustomer_ATS))
suite.addTest(loader.loadTestsFromModule(deleteAppointment_ATS))

runner = unittest.TextTestRunner(verbosity=4)
result = runner.run(suite)

