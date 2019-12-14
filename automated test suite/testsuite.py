import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tests import Forgot_password, Login, Logout, DownloadForm

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTest(loader.loadTestsFromModule(Login))
suite.addTest(loader.loadTestsFromModule(Logout))
suite.addTest(loader.loadTestsFromModule(Forgot_password))
suite.addTest(loader.loadTestsFromModule(DownloadForm))


runner = unittest.TextTestRunner(verbosity=4)
result = runner.run(suite)

